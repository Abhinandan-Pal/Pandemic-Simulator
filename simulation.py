#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:27:19 2020

@author: ap
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

pos = pd.DataFrame()

pos['x'] =[]
pos['y'] =[]
spread_limit = 10
infected = pd.DataFrame()
infected['x'] = []
infected['y'] = []
infected['time'] = []

infected_count = 10
dead_count = 0
recovered_count = 0
for i in range(1000):
    pos.loc[i]=[random.randint(0, 100),random.randint(0, 100)]
        
for i in range(10):
    infected.loc[i]= [pos['x'][i],pos['y'][i],1]
pos = pos.iloc[10:]
pos = pos.reset_index(drop=True)    

def distance(pos1,pos2):
    return ((infected['x'][pos2]-pos['x'][pos1])**2)+((infected['y'][pos2]-pos['y'][pos1])**2)

def day():
    for i in range(len(infected['time'])):
        infected['time'][i]= infected['time'][i] +1
        if (infected['time'][i]>3):
            infected = infected.drop(i)   
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

plt.scatter(pos.x,pos.y)
infected.append([random.randint(0, 1000),1])
