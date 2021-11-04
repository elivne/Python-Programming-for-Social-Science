# Python Programming for Social Science
Code for Python intro module, September 2021, University of Leeds

The two main modules in this repo are `model.py` which is the main running code, and `agentframework.py` which defined the `Agent()` class.
A 300x300 raster is loaded from a CSV file `in.txt`. According to the below argument, agents are placed on it and through several iterations roam the environment and consume resources. They also share with each other if in proximity, and when too full they throw up before continuing to consume.

## How to run the module
Call `model.py` on its own or with all the following 3 arguments (see defaults):
- Number of agents to create (10)
- Number of iterations in which each agent moves, eats and seeks to share (100)
- How near is considered a neighbourhood (20)

At the end of the run, the final state of the environment is saved in a similar format to `out.txt`.

## Ideas for future development
- Consider the values in the raster; if it represents a river then possibly higher/lower values are deeper water, in which case consider which conditions benefit or harm the agents. In other words, the location an agent lands on may effect the agent's life, movement, or ability to consume.
- Derived of above, the model currently starts with a list of agents with an empty store. If initiated with minimum store, and creating situations in which an agent consumes but also starves (because of environmental conditions), then agents can also die or slow down, and in more favourable conditions agents can flourish and move faster.
