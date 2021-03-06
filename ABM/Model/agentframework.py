# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: 200779106
"""
import random

class Agent:
    """
    A class used to represent agents in an agent based model
    
    Attributes:
        
        idnum: int
            The ID number of the agent
        x: int
            The agent's x coordinate
        y: int
            The agent's y coordinate
        environment: list
            A link to a 2D list that contains environment data
        store: int
            The amount of "food" stores the agent has
        agents: list
            A link to a list of all agents
        age:
            The age of the agent. Starts at 0 and increases by one every iteration
            the agent is alive.
        alive:
            A Boolean to keep track of if the agent is alive or dead
        xs:
            A link to a list of x values from the web
        ys:
            A link to a list of y values from the web
    """
    
    def __init__(self, i, environment, agents, td_ys, td_xs, y, x):
        """
        Parameters:
            
            environment: list
                A link to a 2D list that contains environment data
            agents: list
                A link to a list of all agents
            idnum: int
                The ID number of the agent
            colour: str
                The colour that will be used when plotting/animating the agent
        """
        self._idnum = i
        self._x = x
        self._y = y
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.age = 0
        self.alive = True
        self.xs = td_xs
        self.ys = td_ys

    
    def move(self):
        """
        Randomly moves the agent by one step or stays still
        """ 
        # Random walk in the y direction
        rand_y = random.random()
        if rand_y < 0.33:
            self._y = (self._y + 1) % 100
        elif 0.33 <= rand_y < 0.66:
            self._y = (self._y - 1) % 100
        else:
            pass
        
        # Random walk in the x direction
        rand_x = random.random()
        if rand_x < 0.33:
            self._x = (self._x + 1) % 100
        elif 0.33 <= rand_x < 0.66:
            self._x = (self._x - 1) % 100
        else:
            pass
    
       
    def eat(self):
        """
        Checks if the environment where the agent is standing has a value of 
        10 or greater. If so, it subtracts 10 from the environment and adds 
        10 to its own store value
        """ 
        if self.environment[self._x][self._y] > 50:
            self.environment[self._x][self._y] -= 50
            self.store += 10

        
    def distance_between(a, b):
        """
        Calculates and returns the Euclidian distance from one agent to 
        another using Pythagoras' Theorem
        
        Parameters:
            
            a: int
                The first agent
            b: int
                The second agent
            
        Returns:
            
            The distance between the two agents that were input
        """ 
        return (((a._x - b._x)**2) +
        ((a._y - b._y)**2))**0.5
        
    
    def share_with_neighbours(self, neighbourhood):
        """
        Calculates the distance to other agents and if within the 
        neighbourhood distance takes the average of their store value. Both 
        agents' store value is then set to the average
        
        Parameters:
            neighbourhood: int
                The maximum distance to other agents that will result in resources 
                being shared
        """
        for agent in self.agents:
            if agent.alive == True:
                if self.idnum != agent.idnum:
                    distance = self.distance_between(agent)
                    if (distance <= neighbourhood):
                        total = self.store + agent.store
                        avg = total / 3
                        self.store = avg
                        agent.store = avg
                    

    def split(self):
        """
        Creates a new agent and splits the "Parent's" store evenly with the 
        new agent
        """
        # Create the new agent and set the id number as the next number along
        # use the next value from the web page for its x and y coordinates
        newid = len(self.agents)
        if newid < 100:
            xs = int(self.xs[newid].text)
            ys = int(self.ys[newid].text)
            self.agents.append(Agent(newid, self.environment, self.agents, self.ys, self.xs, ys, xs))
        # When the list of coords finishes, use random coords
        else:
            xs = random.randint(0,100)
            ys = random.randint(0,100)
            self.agents.append(Agent(newid, self.environment, self.agents, self.ys, self.xs, ys, xs))
        
        # To split the store between the "parent" and "child"
        avg = self.store / 2
        self.store = avg
        self.agents[newid].store = avg
        
        # To make the "child" spawn at the same location as the "parent"
        # self.agents[newid]._x = self._x
        # self.agents[newid]._y = self._y
        
        
    def reproduce(self):
        """
        Outlines probabilistic conditions for an agent to "reproduce" based 
        on store value
        """
        if self.store > 17 and random.random() < 0.9:
            self.split()
            
        elif self.store > 15 and random.random() < 0.75:
            self.split()
            
        elif self.store > 13 and random.random() < 0.5:
            self.split()
            
        elif self.store > 10 and random.random() < 0.25:
            self.split()
        
        
    def die(self):
        """
        Outlines probabilistic conditions for an agent to "die" based on
        store value
        """
        if self.store < 5 and random.random() < 0.75:
            self.alive = False
            
        elif self.store < 7 and random.random() < 0.5:
            self.alive = False
            
        elif self.store < 10 and random.random() < 0.25:
            self.alive = False
            
        elif self.store < 12 and random.random() < 0.1:
            self.alive = False
    
    
    @property
    def x(self):
        return self._x

    @x.setter
    def setx(self, value):
        self._x = value

    @x.deleter
    def delx(self):
        del self._x
        
        
    @property
    def y(self):
        return self._y

    @y.setter
    def sety(self, value):
        self._y = value

    @y.deleter
    def dely(self):
        del self._y
        
        
    @property
    def idnum(self):
        return self._idnum

    @idnum.setter
    def setidnum(self, value):
        self._idnum = value

    @idnum.deleter
    def delidnum(self):
        del self._idnum
