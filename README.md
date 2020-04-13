# Pandemic-Simulator
This is a program that simulates a pandemic based on parameters and hyper-parameters. It generates a data frame of virtual people. And within the program, these people can move from one community to another. They tend to visit landmarks more often than in other places. And a foreigner could only directly go to the landmark of a different community. When the infection starts spreading the government set up lockdown.But the lock-downs aren't absolute. Many tend to disobey.

## The Dataframes
![alt text](/Images/Population_matrix.png)

The figure represents the population data frame. Each person has an x,y coordinate for their location. A value ranging from 0 to 1. Represent their acceptance of the lockdown. 1 represent going for a perfect lockdown. 0 represents not caring about a lockdown at all. The region represents which region the person belongs to.

![alt text](/Images/infected_matrix.png)

The figure represents the infected data frame. Each person has an x,y coordinate for their location. Time represents the number of days since the person has been infected. The region represents which region the person belongs to.

## The parameters and variables

spread_limit --> Maximum distance between infected and an uninfected person needed for infection to spread<br />
recovery_prob --> Probability that a person will recover from the disease(at least 3 days after infection)<br />
intial_count --> The number of people infected at the very beginning<br />
infection_rate --> Probability of getting infected if within spread_limit<br />
population = --> The number of people at the beginning of the simulation<br />

landmark --> An array storing the x,y coordinates of the landmarks of each region<br />
landmark_prob --> The probability of a random person to visit a landmark on a particular day<br />
landmark_prob_dec_rate --> Rate of decrease in the tendency to visit a landmark on a particular day<br />

lock_ratio --> Initial ratio of people who go on lockdown when government notice is put up<br />
lock_decrease_rate --> ratio of people who go will decrease their lockdown value(Quar) each day<br />
lock_increase_rate --> ratio of people who go will increase their lockdown value(Quar) each day<br />
lock_infected_count --> minimum number of infected people after which lockdown starts<br />

no_of_region --> No. of regions in which the people are divided <br />
![alt text](/Images/variables.png)

# Plots
## General plot
![alt text](/Images/General_plot.png)
Creating a simpler model initially, in this model there are no landmark(every location in equally probable). People don't go into lockdown. The space is not divided into regions. Values of parameters are present in the image itself.
x axis represnts days,and y axis represents no of people.

## Variable Infection_Rate value
![alt text](/Images/infection_rate.png)
This creates several models(simple model as in the General plot) and with different Infection_Rate value. The number of days within which the number of infected people becomes zero are found for each value. And the data is plotted above
![alt text](/Images/infection_rate_people.png)
This creates several models(simple model as in the General plot) and with different Infection_Rate value. The number of people infected and the number of recovered in found for each infection_rate value. And the data is plotted above
