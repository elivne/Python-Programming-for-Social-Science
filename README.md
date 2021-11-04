# Python Programming for Social Science
Code for Python intro module, September 2021, University of Leeds

The two main modules in this repo are `model.py` - the main running code - and the `agentframework.py` which defined the `Agent()` class.
A 300x300 raster is loaded from a CSV file `in.txt`. Agents are placed on it and through several iterations roam the environment and consume resources. They also share with each other, and when too full they throw up before continuing to consume.

# How to run the module
Calling `model.py` on its own or with all the following 3 arguments (see defaults):
- Number of agents to create (10)
- Number of iterations in which each agent moves, eats and seeks to share (100)
- How near is considered a neighbourhood (20)

The final state of the environment is saved in a similar format to `out.txt`.
