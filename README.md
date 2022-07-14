# team_py
Ιn the context of the competition [Space Mission Lab](https://astro-pi.org/mission-space-lab/), each year, teams from different countries plan and schedule a science experiment to run on the International Space Station (ISS). Our team, team.py supported by [ROBOTONIO](https://www.robotonio.gr/), participates for the first time in this competition and chose to experiment with the clouds. How much is climate change affected by clouds? Which clouds amplify the phenomenon of climate change and which ones fight it? In what percentage these clouds are on our planet? Could we control influencing the proportion of these clouds for the benefit of our planet?

## 1. Introduction  
Climate change is an important problem which is currently concerns everyone. That is why our team aimed to investigate how diverse types of clouds affect global warming. During our research, we found out that there are two basic types of clouds: the ones that act like parasols and the ones that act like blankets.
Clouds within a mile or so of Earth’s surface tend to cool more than they warm (parasols). These low, thicker clouds mostly reflect the Sun’s heat. This cools Earth’s surface.
Clouds high up in the atmosphere have the opposite effect: They tend to warm Earth more than they cool (blankets). High, thin clouds trap some of the Sun’s heat. This warms Earth’s surface.
The aim of this scientific experiment was to see if we can measure how many clouds benefit or do not benefit the earth.
We tried to:
•	Classify the blanket and parasol clouds
•	Find the percentage of how much each one covers the earth (based on the orbit of the ISS)
•	Compare our results with past results and
•	Study the distribution of the different cloud categories and how it affects the evolution of the phenomenon of climate change. 

## 2. Method  
Here is the technical part. But primarily, we must talk about the Hardware. Obviously, we used a Raspberry Pi. The only sensors we used were the camera. 
The type of data we wanted was:
•	Images
•	Coordinates of where the picture was taken
We have two phases to the program, the space phase, and the Earth phase. The space phase where we capture the photos from the ISS and the second phase which starts from the point that we receive the photos from the ISS and start analysing them using the Coral and Teachable Machine
We used two methods to analyse the data:
•	Machine learning (Teachable Machine, Coral)
•	OpenCV 
We started with Teachable Machine and Coral for which we imported the data to them to give us an ai model back that could give us the result.
Moving on to the OpenCV part we developed a script to determine how much of the earth's surface was covered by clouds. Also, we used the K-Means algorithm, k-Means uses the distance between points as a measure of similarity, based on k averages (i.e. means).
All our work is freely accessible on GitHub.


## 3. Experiment results  
In the first stage of our experiment, we used coral to classify the images into the above classes. Figure 1 shows the result of the measurements in the two samples. It is important to note that in both samples the same model developed with coral was used, while the percentages refer to a ratio of the number of images per class.
![Figure 1: cloud classes](https://github.com/robotonio/team_py/blob/main/assets/figure_2.png) 
Figure 1: cloud classes
Afterwards a detailed measurement of the percentage of clouds in each image took place, for each category separately, with computer vision techniques and more specifically with the k-means algorithm, with a coefficient K = 8, which emerged as the most appropriate after many experiments. The purpose of this action is to calculate the exact percentage of clouds in each category, as the images classified during the previous stage were not covered by clouds at a rate of 100%.
 
Figure 2: Clouds Classification with Coral
The results of the analysis are shown in Figure 2. In this phase, the images of the "none" class were completely ignored, as the measurement of zero or exceedingly small percentages of clouds, to measure the differences between different time snapshots, we used as samples the photos we collected with our experiment in the 3rd phase of the competition, as well as those provided by the Astro Pi team at the beginning of 2022. For model training, initially we separated some of the images in the classes "none", "blankets" & "parasols", as shown in Figure 1. of undefined class, would not add useful information.

 
Figure 3: Detailed cloud classification with K-mean algorithm
As shown in both graphs above, the percentage of clouds in the "blanket" class prevails to a much higher percentage, which is increased in the second analysis. The distribution of clouds does not change significantly in the two different samples (after all, they are not far apart in time), which we believe is due to some random factors, as the photographs used come from a random and small percentage of our planet's surface.


## 4. Learnings
The idea to participate in the Space Mission Lab impressed us, but at first it scared us a little. What experiment could we do with data from space, without ever dealing with this?
Initially we studied data from the competition, from previous years. We noticed that in most of the photos on our planet there were clouds. Of course, the internet helped a lot. The search began, with the key "clouds" and the idea quickly came: climate change and how it is affected by different types of clouds…
Once we understood the blanket/parasol’ s phenomenon, we designed the different phases of the experiment and shared them to the team. The process of deconstruction of our experiment seemed quite difficult, but very effective, to be able to "break" it in different phases. We also had our first repository on GitHub, the idea and its capabilities impressed us.
We know that the use of more advanced methods, as we write in the conclusion, would give us more reliable results. We look forward to the next time we are given the opportunity to learn new techniques and apply them to deal with a real problem!


## 5. Conclusion  
In both different image samples, the results are not far apart. Although the percentage of coverage was small, we believe that even at a larger scale analysis, the “parasol” clouds will be more than the “blankets”. 
There are certainly many assumptions in our experiment, such as we ignored images with few clouds, we did not measure different types of clouds in the same image, loss of information due to common confident K in the K–means algorithm and impossibility to separate clouds from white surfaces (e.g. snowy areas). One way to deal those problems might be to use more advanced AI techniques, such as Sematic Segmentation or Mono Depth, to identify and measure different types of clouds more accurately in the same image. This is our next target!
But why is the systematic study of this phenomenon important? Knowing that some types of clouds are slowing down the evolution of climate change and others are accelerating it, we believe that an extensive study of the phenomenon will help us to predict climate change-related indicators. Clouds are an important parameter that we should not ignore and why not, in the future we could use it for the benefit of our planet!





## Repository Struction
The project is divided into two parts, the ISS and the Cloud Analysis.

### ISS
In the first part, there is the material that was sent for the third phase of the competition, is the program and the accompanying files that will be run on the ISS for the data collection.

### Cloud Analysis
In the second part, there is the material used for the analysis of the clouds in the requested categories ('parasol' and 'blankets'). In the first phase of the second part, the machine learning technology with the coral is utilized for the categorization of the images, according to the types of clouds. In the second phase, the images are analyzed with computer vision techniques, in order to measure the percentage of clouds in each category that cover the images.
