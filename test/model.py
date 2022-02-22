# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: 200779106
"""
import random
import matplotlib.pyplot as pt
import matplotlib.animation as an
import agentframework
import enviro

# Outlining the starting and stopping conditions of the model and creating
# variables that wil be used throughout
initial = 20
num_of_iterations = 100
neighbourhood = 20
agents = []
colours = ["red","blue","green","yellow","purple","orange","white","black","pink"]
stop = False
fig = pt.figure(figsize=(8,8))
ax = fig.add_axes([0, 0, 1, 1])

# Calling the make_enviro() function from enviro.py
raster = enviro.make_enviro("in.txt")

# Make the agents.
for i in range(initial):
    agents.append(agentframework.Agent(raster, agents, "red"))

# A function to make each frame of the model/animation
def update(frame_number):
    """
    A function to complete all the actions needed for each frame of the model 
    animation. It randomises the list of agents first. It then makes agents 
    move, eat and share resources.

    Parameters
    ----------
    frame_number : int
        The frame number/current iteration of the model. Passed in from 
        stopping() function via matplotlib.animation.FuncAnimation(frames=)

    Returns
    -------
    None

    """
    global stop
    fig.clear()
    
    # Randomise the order of agents
    random.shuffle(agents)

    # Actions (methods) that each agent completes every iteration
    for i in range(agentframework.Agent.num_agents):
        if agents[i].alive == True: 
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            if agents[i].age >= 4:
                agents[i].reproduce()
                agents[i].die()
            
            agents[i].age += 1
            
            # Create the scatter plots limits
            pt.xlim(0, 300)
            pt.ylim(0, 300)
            
            # Plots for those who died this iteration
            if agents[i].alive == False:
                pt.scatter(agents[i].y,agents[i].x,color=agents[i].colour,marker="x")
            
            # plots for living
            else:
                pt.scatter(agents[i].y,agents[i].x,color=agents[i].colour)
        
        # Plots for previously dead (may be better without?)
        elif agents[i].alive == False:
            pt.scatter(agents[i].y,agents[i].x,color=agents[i].colour,marker="x",alpha=0.5)
        
    # Change stop to True if conditions are met for all agents
    # stop = all(agents[i].store <= 500 for i in range(agentframework.Agent.num_agents))
    stop = all(agents[i].alive == False for i in range(agentframework.Agent.num_agents))
    
    pt.imshow(raster)
    

def stopping():
    """
    Defines the stopping conditions for the animation function and yields the 
    the frame/iteration number.
    
    Yields
    ------
    a : int
        The current frame/iteration number

    """
    a=0
    while (a<num_of_iterations) & (not stop):
        yield print(a+1)
        a += 1
    
# Create and show animation of agents
animation = an.FuncAnimation(fig,update,interval=1,frames=stopping,repeat=False)
pt.show()
