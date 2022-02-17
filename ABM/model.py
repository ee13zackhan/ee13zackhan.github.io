# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: ee13zk
"""
import random
import matplotlib.pyplot
import agentframework
import enviro

num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20
agents = []
colours = ["red","blue","green","yellow","purple","orange","white","black"]

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 300, 300])

random.seed(1)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(enviro.environment, agents, i, colours[i%len(colours)]))
    
#    print(f"Agent ID={agents[i].idnum}, y={agents[i].y}, x={agents[i].x}")


# Move the agents, make them eat and make them share.
def update(frame_number):   
    fig.clear()
    # print(f"Frame Number = {frame_number}")
    random.shuffle(agents)
    matplotlib.pyplot.imshow(enviro.environment)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        #print(f"ID = {agents[i].idnum}")
        matplotlib.pyplot.xlim(0, 100)
        matplotlib.pyplot.ylim(0, 100)
       # matplotlib.pyplot.imshow(enviro.environment)
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x, color=agents[i].colour)
        #print(agents[i].y,agents[i].x)
    
        


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
matplotlib.pyplot.show()
# matplotlib.pyplot.xlim(0, 300)
# matplotlib.pyplot.ylim(0, 300)
# matplotlib.pyplot.imshow(enviro.environment)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
# matplotlib.pyplot.show()
