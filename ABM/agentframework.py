# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: ee13zk
"""
import random

class Agent:
    
    """
    Provides methods to instantialise and control agents
    """
    
    
    def __init__(self, environment, agents, idnum, colour):
        self._idnum = idnum
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.colour = colour
    
        """
        Parameters: Environment for agents to interact with, a list of all agents to allow communication with others
        Output: instantialises an agent and links it to the environment and list of all agents
        """
    
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        """
        Parameters: None
        Output: Moves an agent on a random walk in a diagonal path
        """     
       
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        
        """
        Parameters: None
        Output: instructs an agent to eat at the environment
        """
        
    def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a._x - agents_row_b._x)**2) +
        ((agents_row_a._y - agents_row_b._y)**2))**0.5
        
        """
        Parameters: agent 1, agent 2
        Output: returns the distance between the two input agents
        """
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if (self.idnum != agent.idnum) and (distance <= neighbourhood):
                total = self.store + agent.store
                avg = total / 2
                self.store = avg
                agent.store = avg
                # print(f"distance = {str(distance)}, store = {str(self.store)}. My idnum = {str(self.idnum)}, Agent idnum = {str(agent.idnum)}")
            # else:
            #     print("none")
        """
        Parameters: Neighbourhood
        Output: Instructs an agent to share resources with another agent within the neighbourhood distance
        """
        
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
        
        
        

