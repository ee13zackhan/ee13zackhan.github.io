# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: 200779106
"""
import random
import matplotlib.pyplot
import agentframework
import enviro


# Outlining the starting and stopping conditions of the model and creating
# variables that wil be needed throughout.
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
colours = ["red","blue","green","yellow","purple","orange","white","black"]
stop = False
fig = matplotlib.pyplot.figure(figsize=(6,6))
raster = enviro.make_enviro("in.txt")

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(raster, agents, i, colours[i%len(colours)]))

# Define a function to be called for each iteration of the model/animation.
def update(frame_number):   
    fig.clear()
    random.shuffle(agents)
    matplotlib.pyplot.imshow(raster)
    global stop
    
    # Actions (methods) that each agent completes every iteration.
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        # print(f"I am {agents[i].idnum}, my store is {agents[i].store}")
        
        # Create the scatter plots for each agent.
        matplotlib.pyplot.xlim(0, 100)
        matplotlib.pyplot.ylim(0, 100)
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x, color=agents[i].colour)
        
    # Change stop to True if store conditions are met for all agents.
    stop = all(agents[i].store >= 100 for i in range(num_of_agents))
    
# Generator function to define stopping conditions for animation.
def stopping():
    a=0
    while (a<num_of_iterations) & (not stop):
        yield a
        a += 1
    
# Create and show animation of agents
animation = matplotlib.animation.FuncAnimation(fig,update,interval=1,frames=num_of_iterations,repeat=False)
matplotlib.pyplot.show()
