# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:51:14 2021

This module defines the class Agent.
An instance of Agent is initiated with random x,y values (location) on a grid. 
Agent has a method to move 1 step in a random, diagonal direction.

@author: Eran Livne
"""
# imports
import random

# old global board size constant; replaced with environment size
#BOARD_SIZE = 100

class Agent():
    """
    The Agent class is interacting with other agents and a shared environment.
    Its constructor take the shared environment.
    Each agent has an x,y location and store of food.
    An agent can move one diagonal step, eat foor and throw it up
    """

    def __init__(self, environment, agents):
        """
        Initialises an Agent instance with a link to the shared environment,
        list of agents, a random x,y location in the environment and empty
        internal store.

        Parameters
        ----------
        environment : list
            Shared environment.
        
        agents : list
            All agents

        Returns
        -------
        None.
        """
        self.env = environment
        self.agents = agents
        self._y = random.randint(0,len(self.env)-1)
        self._x = random.randint(0,len(self.env[0])-1)
        self._store = 0
    
    # Defining accessor methods for x,y as read-only properties
    @property
    def x(self):
        return self._x;

    @property    
    def y(self):
        return self._y;
    
    # Define accessor and modifier for store
    def getStore(self):
        return self._store
    
    def setStore(self, value):
        self._store = value
    
    store = property(fget=getStore, fset=setStore, doc="Agent\'s store")
    
    def move(self):
        """
        This method ramndomly changes both x and y values by +/-1
        i.e. moves the Agent in one of four diagonal directions 
        and accounts for boundaries of the environment.

        Parameters
        -------
        None.
        
        Returns
        -------
        None.

        """
        self._y = (self._y+1) % len(self.env) if random.random() < 0.5 \
            else (self._y-1) % len(self.env)
        self._x = (self._x+1) % len(self.env[0]) if random.random() < 0.5 \
            else (self._x-1) % len(self.env[0])
    
    def eat(self):
        """
        This method makes Agent eat 10 from the environment (or less, if left).
        Agent throws up if its store passes a sick level of 100.
        
        Parameters
        -------
        None.


        Returns
        -------
        None.

        """
        eat_value = 10 # set eating chunks
        
        if self.env[self._y][self._x] > eat_value:
            self.env[self._y][self._x] -= eat_value
            self._store += eat_value
        else: # if less that eat_value, eat whatever is left
            self._store += self.env[self._y][self._x]
            self.env[self._y][self._x] = 0
            #TEST make sure we were here - takes many iterations
            #print(self)
        
        # Check if _store is too high and throw it up
        sick_level = 100
        if self._store >= sick_level:
            self.env[self._y][self._x] = self._store
            self._store = 0
            #TEST make sure we were here (more than 10 iterations)
            #print(self)
        # End if
    
    def share(self, neighbourhood):
        """
        This method finds nearby agents to share food with equally.

        Parameters
        ----------
        neighbourhood : int
            Proximity considered to be a neighbourhood.

        Returns
        -------
        None.

        """
        # Test this was called
        #print(neighbourhood)
        
        # Loop through all agents
        for other_agent in self.agents:
            # Find other agents who are near
            if self is not other_agent and \
             self.distanceBetween(other_agent) <= neighbourhood:
                # share store equally (both get average)
                #print(self, other_agent) # test before
                avg = (self._store + other_agent.store) / 2
                self._store = other_agent.store = avg
                #print(self, other_agent) # test after
            # End if
        # End loop

    def distanceBetween(self, agent):
        """
        Find our distance between self and another agent

        Parameters
        ----------
        agent : Object
            Another agent.

        Returns
        -------
        distance : float.

        """
        return ((agent.y - self.y) ** 2 + (agent.x - self.x) ** 2) ** 0.5

            
    def __str__(self):
        """
        Overridden str function to display Agent location and store info.

        Returns
        -------
        String
            Current coordinates and store of Agent.

        """
        return "Agent at coordinates ({0},{1}); store: {2}".format(self._x, \
                self._y, self._store)
