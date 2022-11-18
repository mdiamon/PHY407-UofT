"""
This program simulates Brownian motion in the presence of walls
Note that the physical behaviour would be to stick to walls,
which is the purpose of Q1a.
Author: Nico Grisouard, University of Toronto
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


def nextmove(x, y):
    """ randomly choose a direction
    0 = up, 1 = down, 2 = left, 3 = right"""
    direction =  # COMPLETE

    if direction == 0:  # move up
        y += 1
    elif direction == 1:  # move down
        y -= 1
    elif direction == 2:  # move right
        x += 1
    elif direction == 3:  # move left
        x -= 1
    else:
        print("error: direction isn't 0-3")

    return x, y


font = {'family': 'DejaVu Sans', 'size': 14}  # adjust fonts
rc('font', **font)


# %% main program starts here ------------------------------------------------|
# YOU NEED TO FINISH IT!

plt.ion()

Lp = 101  # size of domain
Nt = 5000  # number of time steps
# arrays to record the trajectory of the particle
# COMPLETE

centre_point = (Lp-1)//2  # middle point of domain
xp = centre_point
yp = centre_point

for i range(Nt):
    xpp, ypp = nextmove(xp, yp)
    # AND OFF YOU GO!
