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
# variables that wil be used throughout.
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
colours = ["red","blue","green","yellow","purple","orange","white","black"]
stop = False
fig = matplotlib.pyplot.figure(figsize=(6,6))

# Calling the make_enviro() function from enviro.py
raster = enviro.make_enviro("in.txt")

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(raster, agents, i, colours[i%len(colours)]))

# A function to make each frame of the model/animation.
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
    
    # Actions (methods) that each agent completes every iteration.
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        # Create the scatter plots for each agent.
        matplotlib.pyplot.xlim(0, 100)
        matplotlib.pyplot.ylim(0, 100)
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x, color=agents[i].colour)
        
    # Change stop to True if store conditions are met for all agents.
    stop = all(agents[i].store >= 100 for i in range(num_of_agents))
    matplotlib.pyplot.imshow(raster)
    

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
        yield a
        a += 1
    
# Create and show animation of agents
animation = matplotlib.animation.FuncAnimation(fig,update,interval=1,frames=num_of_iterations,repeat=False)
matplotlib.pyplot.show()
