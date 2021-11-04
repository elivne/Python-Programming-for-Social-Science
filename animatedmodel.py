"""
Created on Mon Nov 04 09:51:22 2021

Parallel model to run the environment on an animated screen:
creates agents in an environment read from a 
CSV file 'in.txt', then makes them move, consume and share resources.

Arguments
---------
number_of_agents : int [default 10]
number_of_iterations : int [def -1 = random]
neighbourhood_proximity : int [def 20]

Output
------
Final state of environment is written as CSV to 'out.txt'.

@author: Eran Livne
"""
# Imports
import random
import sys
import csv
import agentframework
import matplotlib.pyplot
import matplotlib.animation 

# Read command line arguments or set defaults (tested via config)
if len(sys.argv) == 4:
    num_of_agents = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])
else:
    # No arguments or wrong number of arguments - set defaults
    num_of_agents = 10
    num_of_iterations = -1
    neighbourhood = 20
    if len(sys.argv) > 1:
        print("Wrong number of arguments. Defaults set.")
    
# Test the values
# Known issue: num of iterations 0 counts as 1
print("The model will create " + str(num_of_agents) + " agents and run for " \
      + (str(num_of_iterations) if num_of_iterations >= 0 else "random") \
      + " iterations. Neighbourhood proximity: " + str(neighbourhood))    
    
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

# Create list of agents
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Set axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Boolean to continue iterations
carry_on = True	

# Updating the frame - called repeatedly for animation	
def update(frame_number):
    
    # Clear the animation
    fig.clear()
    
    # Plot environment
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.xlim(0, len(environment[0]))
    matplotlib.pyplot.imshow(environment)
    
    # Shuffle the agent list between iterations
    random.shuffle(agents)
    # Loop through (shuffled) agents and activate each
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share(neighbourhood)
    # End for

    # Global variables to control iterations
    global carry_on
    global num_of_iterations

    # End the run after given number of iterations or randomly
    if num_of_iterations > 0:
        num_of_iterations -= 1
    elif num_of_iterations == 0:
        carry_on = False
        print("Completed the requested number of iterations.")
    elif random.random() < 0.1:
        carry_on = False
        print("Reached the random stopping condition.")
    
    # Plot agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# Function serving the animation (next frame to be called)		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# Set and launch animation
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, \
                                               repeat=False)

# Display
matplotlib.pyplot.show()
