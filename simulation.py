import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

spread_limit = 10
recovery_prob = 0.70
intial_count = 10

pos = pd.DataFrame()
pos['x'] =[]
pos['y'] =[]

infected = pd.DataFrame()
infected['x'] = []
infected['y'] = []
infected['time'] = []

infected_count = intial_count
dead_count = 0
recovered_count = 0


infected_count_arr = []
dead_count_arr = []
recovered_count_arr = []
non_infected_count_arr = []

for i in range(1000):
    pos.loc[i]=[random.randint(0, 100),random.randint(0, 100)]


for i in range(10):
    infected.loc[i]= [pos['x'][i],pos['y'][i],1]

pos = pos.iloc[10:]
pos = pos.reset_index(drop=True)    

def distance(pos1,pos2):
    return ((infected['x'][pos2]-pos['x'][pos1])**2)+((infected['y'][pos2]-pos['y'][pos1])**2)


def day():
    global infected_count,dead_count,recovered_count,infected,pos
    infected_count_arr.append(infected_count)
    non_infected_count_arr.append(len(pos['x']))
    dead_count_arr.append(dead_count)
    recovered_count_arr.append(recovered_count)
    for i in range(len(infected['time'])):
        infected['time'][i]= infected['time'][i] +1
        if (infected['time'][i]>3):
            infected = infected.drop(i)
            removed()
    infected = infected.reset_index(drop=True)
    infected_count = len(infected['time'])  
    i = 0
    while(i < len(pos['x'])):
        for j in range(infected_count):
            if(distance(i,j)< spread_limit):
                infected.loc[infected_count]= [pos['x'][i],pos['y'][i],1]
                infected_count = infected_count + 1   
                pos = pos.drop(i)
                pos = pos.reset_index(drop=True) 
        
        i = i +1       

def removed():
    if(random.random()<recovery_prob):
        global recovered_count
        recovered_count = recovered_count + 1
    else :
        global dead_count
        dead_count = dead_count + 1


while(infected_count != 0 ):
    day()


txt="spread_limit = {}  recovery_prob = {} intial_count = {}".format(spread_limit,recovery_prob,intial_count)
fig = plt.figure(figsize=(len(dead_count_arr), 5))
ax = fig.add_subplot(111)
ax.plot(dead_count_arr,color='blue')

ax.plot(infected_count_arr,color='orange' )
ax.plot(recovered_count_arr,color='green')
plt.gca().legend(['Dead', 'infected', 'recovered'], loc='best')
plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
ax.show()