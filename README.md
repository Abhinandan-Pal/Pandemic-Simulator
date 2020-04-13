# Pandemic-Simulator
This is a program that simulates a pandemic based on parameters and hyper-parameters. It generates a data frame of virtual people. And within the program, these people can move from one community to another. They tend to visit landmarks more often than in other places. And a foreigner could only directly go to the landmark of a different community. When the infection starts spreading the government set up lockdown.But the lock-downs aren't absolute. Many tend to disobey.

## The Dataframes
![alt text](/Images/Population_matrix.png)

The figure represents the population data frame. Each person has an x,y coordinate for their location. A value ranging from 0 to 1. Represent their acceptance of the lockdown. 1 represent going for a perfect lockdown. 0 represents not caring about a lockdown at all. The region represents which region the person belongs to.

![alt text](/Images/infected_matrix.png)

The figure represents the infected data frame. Each person has an x,y coordinate for their location. Time represents the number of days since the person has been infected. The region represents which region the person belongs to.
