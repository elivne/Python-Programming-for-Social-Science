# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:51:22 2021

Model running the main script: creates agents in an environment read from a 
CSV file 'in.txt', then makes them move, consume and share resources.

Arguments
---------
number_of_agents : int [default 10]
number_of_iterations : int [def 100]
neighbourhood_proximity : int [def 20]

Output
------
Final state of environment is written as CSV to 'out.txt'.

@author: Eran Livne
"""
# Imports
import random
import time
import sys
import csv
import agentframework
import matplotlib.pyplot

# Set the random seed for reproducibility
#random.seed(1)

# Test run time - save start time
time_start = time.time()

# Read command line arguments or set defaults (tested via config)
if len(sys.argv) == 4:
    num_of_agents = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])
else:
    # No arguments or wrong number of arguments - setting defaults
    num_of_agents = 10
    num_of_iterations = 100
    neighbourhood = 20
    if len(sys.argv) > 1:
        print("Wrong number of arguments.")
    
# Test the values
print("The model will create " + str(num_of_agents) + " agents and run " + \
      "for " + str(num_of_iterations) + " iterations. " + \
      "Neighbourhood proximity: " + str(neighbourhood))

# Read in.txt file into an evironment list
f = open("in.txt", newline='')
freader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in freader: # Loop through rows in the file
    rowlist = []
    for value in row: # Loop though values in each row
        rowlist.append(int(value)) # read as integers
    environment.append(rowlist)
f.close()

# Test that environment is an even grid - same number of values in every row
#for row in range(len(environment)):
#    if len(environment[row]) != len(environment[0]):
#        print(len(environment[row]))

# Test plot the environment
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

# Create list of agents
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Test/log initial locations
#print(agents)

# Repeat for number of iterations
for j in range(num_of_iterations):
    # Shuffle the agent list between iterations
    random.shuffle(agents)
    # Loop through (shuffled) agents and activate each
    for i in range(num_of_agents):
        #print(agents[i]) # test before and after location and store
        agents[i].move()
        agents[i].eat()
        agents[i].share(neighbourhood)
        #print(agents[i])
    # End for
# End for

# Test/log final locations
#print(agents[0])


''' OLD TEST - REPLACED OLD FUNCTION WITH AGENT METHOD
# Find min and max distances:
# Start with maximal minimum and minimal maximum
min_distance = 100
max_distance = 0
# Loop through agents excluding last one
for i in range(num_of_agents-1):
    # Loop from one after i to last one (avoid checking distances twice)
    for j in range(i+1, num_of_agents):
        # Adjust min and max if needed
        min_distance = min(min_distance,agents[i].distanceBetween(agents[j]))
        max_distance = max(max_distance,agents[i].distanceBetween(agents[j]))

# log min and max distances
print("min distance", min_distance, "max distance", max_distance)
'''

# Plot environment
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.imshow(environment)

# Plot agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#matplotlib.pyplot.scatter(maxpoint[1],maxpoint[0], color='red')
matplotlib.pyplot.show()

# Write environment to an out.txt file
f2 = open("out.txt", 'w', newline='')
fwriter = csv.writer(f2, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in environment: # Loop through rows in environment
    fwriter.writerow(row)
f2.close()

# Test run time - save end time and log result
time_end = time.time()
print("Runtime = " + str(time_end - time_start))
