# team_py
Ιn the context of the competition [Space Mission Lab](https://astro-pi.org/mission-space-lab/), each year, teams from different countries plan and schedule a science experiment to run on the International Space Station (ISS). Our team, team.py supported by [ROBOTONIO](https://www.robotonio.gr/), participates for the first time in this competition and chose to experiment with the clouds. How much is climate change affected by clouds? Which clouds amplify the phenomenon of climate change and which ones fight it? In what percentage these clouds are on our planet? Could we control influencing the proportion of these clouds for the benefit of our planet?

## Idea
Clouds can act like a parasol, cooling the Earth by reflecting sunlight away from the planet’s surface and back into space. But they can also act like an insulating blanket, warming the Earth by preventing some of the heat in our atmosphere from escaping into space as infrared radiation. This “blanket” effect is particularly noticeable during the winter, when cloudy nights are typically much warmer than cloud-free ones. Which of these two effects dominates – parasol or blanket – depends on the altitude and thickness of the clouds. As a general rule, the higher a cloud is, the more effective it is at preventing heat from escaping into space. The thicker a cloud is, the better it is at reflecting sunlight away from Earth’s surface.

Global warming is expected to cause changes in the amount of cloud cover, and the height and thickness of these clouds in the future, shifting the balance between the parasol and blanket effects of clouds. The knock-on effect this will have on temperature is known as cloud feedback. Climate change projections cannot ignore cloud feedback, as even relatively small changes in cloud properties can have significant implications for global temperature.

Our idea is to develop a program that will try to classify clouds according to their altitude and thickness, in order to investigate whether these two phenomena affect, positively or negatively, climate change. The same system could be applied to historical data, from previous missions, in order to study the (possible) rate of change of balance between the parasol and blanket effects of clouds and how this change affects the current forecasts for rising temperatures on our planet due to climate change.

Our idea will give us the opportunity to take advantage of the latest equipment upgrades. Specifically, by using the camera we will receive photos from all the way. With computer vision techniques we will process the images as needed and with machine learning, after we train our program to recognize the density of the clouds, we will feed it with the newest photos that we will take. For the purpose of comparison with historical data, we will store for each photo and additional information, such as coordinates, time, etc.

## Project
The project is divided into two parts, the ISS and the Cloud Analysis.

### ISS
In the first part, there is the material that was sent for the third phase of the competition, is the program and the accompanying files that will be run on the ISS for the data collection.

### Cloud Analysis
In the second part, there is the material used for the analysis of the clouds in the requested categories ('parasol' and 'blankets'). In the first phase of the second part, the machine learning technology with the coral is utilized for the categorization of the images, according to the types of clouds. In the second phase, the images are analyzed with computer vision techniques, in order to measure the percentage of clouds in each category that cover the images.
