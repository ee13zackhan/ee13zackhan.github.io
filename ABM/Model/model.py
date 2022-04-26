# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: 200779106
"""
# import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot as pt
import matplotlib.animation as an
import requests
import bs4
import random

import agentframework
import enviro



# Change the required debugging variable to True when debugging. This will 
# cause information to be printed to the console to aid with debugging and 
# checking if the code works as expected
# Debugging Variables:
WEB = False
ITERATIONS = False
AGENTS = False
SHUFFLE = False
COORD = False
# random.seed(1)

# Outlining the starting and stopping conditions of the model and creating
# variables that wil be used throughout
initial = 20
if AGENTS == True:
    print(f"The initial number of agents is set to {initial}")
num_of_iterations = 100
if ITERATIONS == True:
    print(f"The max number of iterations is {num_of_iterations}")
neighbourhood = 20
agents = []
stop = False
if ITERATIONS == True:
    print(f"stop is initially {stop}")
fig = pt.figure(figsize=(8,8))
ax = fig.add_axes([0, 0, 1, 1])

# Calling the make_enviro() function from enviro.py
raster = enviro.make_enviro("in.txt")

# Get x and y data from the webpage below
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
# Create an array each for the x and y values (includes HTML)
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
if WEB == True:
    print(f"The first td_ys value is: {td_ys[0]}")
    print(f"The first td_xs value is: {td_xs[0]}")

# Make the agents using the values from the td_ys and td_xs as the starting position
for i in range(initial):
    # Read the x and y values from the arrays as an integer and ignoring HTML
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    if WEB == True:
        print(f"The starting coordinates are ({x},{y}) for agent {i}")
    agents.append(agentframework.Agent(i, raster, agents, td_ys, td_xs, y, x))
    
    
if COORD == True:
    for i in range(len(agents)):
        ix = agents[i].x
        iy = agents[i].y
        print(f"The initial coordinates for agent {i} are ({ix},{iy})")
    
if AGENTS == True:
    print(f"There are actually {len(agents)} agent(s)")
    
if SHUFFLE == True:
    initial_order = []
    for i in range(len(agents)):
        initial_order.append(agents[i].idnum)
    print(f"The initial order of agents is {initial_order}")
    
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
    if SHUFFLE == True:
        order = []
        for i in range(len(agents)):
            order.append(agents[i].idnum)
        print("The order of agents for this iteration is:")
        print(order)

    # Actions (methods) that living agents complete every iteration
    for i in range(len(agents)):
        if agents[i].alive == True: 
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            # Actions that require a certain age go here
            if agents[i].age >= 4:
                agents[i].reproduce()
                agents[i].die()
            
            # Make the agents age 1 unit
            agents[i].age += 1
            
            
            # Plots for those who died this iteration
            if agents[i].alive == False:
                pt.scatter(agents[i].y,agents[i].x,color="red",marker="x")
            
            # plots for living
            else:
                pt.scatter(agents[i].y,agents[i].x,color="white")
        
        # Plots for previously dead
        # elif agents[i].alive == False:
        #     pt.scatter(agents[i].y,agents[i].x,color=agents[i].colour,marker="x",alpha=0.5)
        
    # Change stop to True if conditions are met for all agents
    stop = all(agents[i].alive == False for i in range(len(agents)))

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

        yield a
        if ITERATIONS == True:
            print(f"Iteration: {a}")
            print(f"stop is {stop}")
        a += 1
    
# Create and show animation of agents
def run():
    """
    Creates the model animation
    """
    animation = an.FuncAnimation(fig,update,interval=1,frames=stopping,repeat=False)
    canvas.draw()

# Create a GUI which has the ability to call the function "run()" 
root = tkinter.Tk()
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master=root)
canvas._tkcanvas.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)


tkinter.mainloop()










