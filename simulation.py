# PLEASE READ ATTENTION BEFORE EXECUTING
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

spread_limit = 1
recovery_prob = 0.70
intial_count = 10
infection_rate = 0.5
population = 1000
def initialize():
    global infected_count,dead_count,recovered_count,infected,pos,infected_count_arr,dead_count_arr,recovered_count_arr,non_infected_count_arr 
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

    for i in range(population):
        pos.loc[i]=[random.randint(0, population/10),random.randint(0, population/10)]


    for i in range(10):
        infected.loc[i]= [pos['x'][i],pos['y'][i],1]

    pos = pos.iloc[10:]
    pos = pos.reset_index(drop=True)    

def distance(pos1,pos2):
    return ((infected['x'][pos2]-pos['x'][pos1])**2)+((infected['y'][pos2]-pos['y'][pos1])**2)

def infected_check():
    return (random.random()<infection_rate)

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
            if(i>=len(pos['x'])):
                break
            if(distance(i,j)< spread_limit):
                if(infected_check()):
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

def day_call():
    initialize()
    while(infected_count != 0 ):
        day()
        
#*************************************ATTENTION******************************************************
#PLEASE DON'T EXECUTE THE CODE ALL AT ONCE RUN THE FIRST HALF FIRST AND THE SECOND HALF ONE AT A TIME        
#*************************************ATTENTION******************************************************

################################################################################################################################################
# Get plot an data for a virtual environment of a given parameter
################################################################################################################################################
day_call()

txt="spread_limit = {}  recovery_prob = {} intial_count = {} infection_rate = {} ".format(spread_limit,recovery_prob,intial_count,infection_rate)
fig = plt.figure(figsize=(len(dead_count_arr), 5))
ax = fig.add_subplot(111)
ax.plot(dead_count_arr,color='blue')
ax.plot(non_infected_count_arr,color='orange' )
ax.plot(infected_count_arr,color='red' )
ax.plot(recovered_count_arr,color='green')

plt.gca().legend(['Dead', 'non infected','infected', 'recovered'], loc='best')
plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
#plt.savefig(txt+ ".pdf")
ax.show()

################################################################################################################################################
# Change in total involved,safe,and days taken with spread_limit_change
################################################################################################################################################
total_involed = []
total_safe = []
days = []
spread_limit_values = []
def spread_limit_change():
    global spread_limit
    spread_limit = 1
    for i in range(16):    
        day_call()
        total_involed.append(recovered_count + dead_count)
        total_safe.append(population - recovered_count - dead_count)
        days.append(len(recovered_count_arr))
        spread_limit_values.append(spread_limit)
        spread_limit = spread_limit + 1
    
spread_limit_change()

txt="PEOPLE SPREAD_LIMIT_VARIABLE(1,16)  recovery_prob = {} intial_count = {} infection_rate = {} ".format(recovery_prob,intial_count,infection_rate)
plt.plot(spread_limit_values,total_involed ,color='blue')
plt.plot(spread_limit_values,total_safe,color='orange' )
plt.xlabel("SPREAD_LIMIT_VALUE")
plt.ylabel("No. of people")
plt.legend(['total_involed', 'total_safe'], loc='best')
plt.title( txt)
plt.savefig(txt+ ".pdf")
plt.show()

txt="DAYS SPREAD_LIMIT_VARIABLE(1,16)  recovery_prob = {} intial_count = {} infection_rate = {} ".format(recovery_prob,intial_count,infection_rate)
plt.plot(spread_limit_values,days)
plt.xlabel("SPREAD_LIMIT_VALUE")
plt.ylabel("Days")
plt.title( txt)
plt.savefig(txt+ ".pdf")
plt.show()


