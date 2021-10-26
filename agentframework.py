# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:42:08 2021

@author: Katie Weir
"""

import random

class Agent():
    
    def __init__(self, i, agents, environment, rows, cols, y=None, x=None):
        #self.y = None
        #self.x = None
        self.i = i
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.rows = rows
        self.cols = cols
        if (y == None):
            self.y = random.randint(0, 99)
        else:
            self.y = y
        if (x == None):
            self.x = random.randint(0, 99)
        else:
            self.x = x
        
    
    def __str__(self):
        #Standard string method, so that if you try to print an agent object
        #it will return something human readable, as defined by the code
        #below, so you can check on the status of the agent, rather than
        #just printing the agent's memory address.
        #This will print the x and y coords, and the store value of each agent
        return "Agent id=" + str(self.i) + ", x=" + str(self.x) \
            + ", y=" + str(self.y) \
            + ", store=" + str(self.store)
        
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.rows
        else:
            self.y = (self.y - 1) % self.rows

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.cols
        else:
            self.x = (self.x - 1) % self.cols
            
            
    def eat(self):
        #If the environment is higher than 10 units, eat 10 units and add to
        #agent's belly store
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            #Else if the environment is not greater than or equal to 10, eat
            #the environment down to zero height
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        #If belly is fuller than 100 units, chunder, and reset belly to zero
        if self.store >= 100:
            print("I have done a chunder")
            self.environment[self.y][self.x] += 100
            self.store = 0
            
        
    def distance_between(self, b):
        #Use Pthagoras' theorem to calculate the distance between self and
        #another agent, b
        return (((self.x - b.x)**2) + ((self.y - b.y)**2))**0.5
            
            
    def share_with_neighbours(self, neighbourhood):
        #If the agent is close enough to any other agent(s), as defined by the
        #neighbourhood variable, then average their individual store variables
        
        for i in range(len(self.agents)):
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(self.agents[i])
            # If distance is less than or equal to the neighbourhood
            if distance < neighbourhood:
                print("Agent distance is", distance, "therefore sharing store")
                # Sum self.store and agent.store .
                #Finding the average of the agents shared stores.
                total = self.store + self.agents[i].store
                # Divide sum by two to calculate average.
                average = total / 2
                # self.store = average
                self.store = average
                # agent.store = average
                self.agents[i].store = average
