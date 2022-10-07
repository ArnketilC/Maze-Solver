import numpy as np

maze = ''

with open('maze') as f:
    maze = f.readlines()
    maze = [line.rstrip() for line in maze]

print(maze)