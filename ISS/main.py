'''
Space Mission Lab - Phase 2
Team: team_py
Country: Greece
School: ROBOTONIO
Mentor: Tassos Kasmiris
Students:
    Tasos Makrostergios
    Andreas Tsounias
    George Tsaligopoulos
    Chris Megagiannis
    Vlasis Vlasopoulos
Misssion:
    Collect data for processing in the next phase
'''
#Import modules
from ast import Try
from pathlib import Path
from skyfield.api import load
from logzero import logger, logfile
from sense_hat import SenseHat
from picamera import PiCamera
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv

def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Counter", "Date/time", "Latitude", "Longitude", "Sunlight")
        writer.writerow(header)

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def convert(angle):
    """
    Convert a `skyfield` Angle to an EXIF-appropriate
    representation (rationals)
    e.g. 98° 34' 58.7 to "98/1,34/1,587/10"

    Return a tuple containing a boolean and the converted angle,
    with the boolean indicating if the angle is negative.
    """
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    location = ISS.coordinates()

    # Convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = convert(location.latitude)
    west, exif_longitude = convert(location.longitude)

    # Set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # Capture the image
    camera.capture(image)

# Get base main folder
base_folder = Path(__file__).parent.resolve()

# ephemeris initialization (the file de421.bsp MUST be on the project folder)
ephemeris = load('de421.bsp')
timescale = load.timescale()

# Set a logfile name
logfile(base_folder/"events.log")


# Set up camera
cam = PiCamera()
cam.resolution = (2592, 1944)

# Initialise the CSV file
data_file = base_folder/"data.csv"
create_csv_file(data_file)

# Initialise the photo counter
counter = 1
# Record the start, current and last capture time
start_time = datetime.now()
now_time = datetime.now()
capture_time = datetime.now()
# Run a loop for (almost) three hours
while (now_time < start_time + timedelta(minutes=178)):
    try:
        # Check to capture image every 18 seconds
        if now_time > capture_time + timedelta(seconds=18):
            t = timescale.now()
            # If it's day, capture the image
            if ISS.at(t).is_sunlit(ephemeris):
                #print("In sunlight")                
                # Get coordinates of location on Earth below the ISS
                location = ISS.coordinates()
                # Save the data to the file
                data = (
                    counter,
                    datetime.now(),
                    location.latitude.degrees,
                    location.longitude.degrees,
                    "1",
                )
                add_csv_data(data_file, data)
                # Capture image
                image_file = f"{base_folder}/photo_{counter:03d}.jpg"
                capture(cam, image_file)
                # Log event
                logger.info(f"iteration {counter}")
                # Update counter
                counter += 1
                # Update the capture time
                capture_time = datetime.now()
            # If it's night, capture image every 40 seconds
            elif now_time > capture_time + timedelta(seconds=40):
                #print("In darkness")
                # Get coordinates of location on Earth below the ISS
                location = ISS.coordinates()
                # Save the data to the file
                data = (
                    counter,
                    datetime.now(),
                    location.latitude.degrees,
                    location.longitude.degrees,
                    "0",
                )
                add_csv_data(data_file, data)
                # Capture image
                image_file = f"{base_folder}/photo_{counter:03d}.jpg"
                capture(cam, image_file)
                # Log event
                logger.info(f"iteration {counter}")
                # Update counter
                counter += 1
                # Update the capture time
                capture_time = datetime.now()
        # Update the current time
        now_time = datetime.now()

        
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')
