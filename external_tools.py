"""
python has 2 types of packages:
1. built-in
2. external
Built-in - comes with python installation.
External - needs to be installed using pip commnand.
"""

"""
Important terminologies:
1. module - a single python file
2. package - a collection of modules
3. function - a reusable bloack of code
4. class - a blueprint for creating objects

Think of it like this:
1. module - a toolbox
2. package - a garage with multiple toolboxes
3. function - a tool in the toolbox
4. class - a blueprint for creating tools
"""

#builtin module
import math

#sqrt is a function inside math module
root=math.sqrt(16)
print(root)

#we can also import specific functions from a module
from math import sqrt, pi

root=sqrt(25)
print(root)

import random

number=random.randint(1,10)
choice=random.choice(['apple','blueberry','strawberry'])
print(number)
print(choice)

import os
current_directory=os.getcwd()
print(current_directory)


