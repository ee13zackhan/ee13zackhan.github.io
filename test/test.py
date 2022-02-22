# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: 200779106
"""
import random
import matplotlib.pyplot as pt
import agentframework
import enviro

random.seed(1)

# Outlining the starting and stopping conditions of the model and creating
# variables that wil be used throughout.
initial = 20
num_of_iterations = 10
neighbourhood = 20
agents = []
colours = ["red","blue","green","yellow","purple","orange","white","black"]
stop = False
it = 1

# Calling the make_enviro() function from enviro.py
raster = enviro.make_enviro("in.txt")

# Make the agents.
for i in range(initial):
    agents.append(agentframework.Agent(raster, agents, colours[i%len(colours)]))

for j in range(num_of_iterations):
# Randomise the order of agents
    random.shuffle(agents)
    print(it)
    it += 1
    
    # Actions (methods) that each agent completes every iteration.
    for i in range(agentframework.Agent.num_agents):
        if agents[i].alive == True: 
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            if agents[i].age > 5:
                agents[i].reproduce()
                agents[i].die()
            
            agents[i].age += 1
            
            # Create the scatter plots for each agent.
            pt.xlim(0, 300)
            pt.ylim(0, 300)
            
            if agents[i].alive == False:
                pt.scatter(agents[i].y,agents[i].x,color=agents[i].colour,marker="x")
            else:
                pt.scatter(agents[i].y,agents[i].x,color=agents[i].colour)
           
        elif agents[i].alive == False:
            pt.scatter(agents[i].y,agents[i].x,color=agents[i].colour,marker="x")

    
    pt.imshow(raster)
    pt.show()

