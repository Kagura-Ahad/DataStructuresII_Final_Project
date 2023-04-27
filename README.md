# DataStructuresII_Final_Project
Spring_2023-Data_StructuresII-FinalProject 

Why do I need a Temperature Monitoring System?
>I am a landlord trying to grow a plant that will flower in two months which is usually grown in the current season. 
The specification I need to grow for that plant is that the temperature conditions it is going through should not fluctuate that much throughout the day. 
Assuming that the season for the past 10 days will remain the same for the upcoming two months, I decide to take the fluctuations of each day of past one month of all of the greenhouses I own, average them, such that I get the average fluctuations for the past one month for all of my greenhouses, and then decide in which greenhouse do I plant that plant.

Why Temperature monitoring system using Fingertree?
>1)Can get overall first and last values of temperatures in O (1)

>2)Can get first and last values of temperatures in a specified range in O (K+1) ~ O(K)

>3)Can search for a certain temperature in O (log(n))

>4)Can search for a certain temperature in O (log(n)+k)
>
If I use a fingertree instance to store the hourly temperatures of each day of each greenhouse for the past 30 days, I can access the temperature of the first and the last hour of each day very quickly and then I can calculate the difference in them to get my fluctuations of each day of each greenhouse of the past 30 days. 
Then I can average those 30 fluctuations for each greenhouse and then can decide which greenhouse has suitable average fluctuation for my plant to grow.
