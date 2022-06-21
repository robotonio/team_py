# ISS Part

main.py is the source file of the program, that ran in the iss, in order to collect the data used in the last phase of the analysis. It is basically a simple program that runs for about three hours and every 18 seconds when it is day, and every 40 seconds when it is night, it takes a photo and saves the image in a folder. For each photo, it stores in a separate file the necessary information, such as time of photography and geographical coordinates.

The file de421.bsp MUST be on the project folder (in the same folder as the main), as it is used to check the program, whether it is day or night at the point of photo shooting.
