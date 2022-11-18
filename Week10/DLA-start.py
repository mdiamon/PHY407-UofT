"""
This program simulates diffusion limited aggregation on an LxL grid.
Particles are initiated until the centre point is filled.
Author: Nico Grisouard, University of Toronto
Based on Paul J Kushner's DAL-eample.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


def nextmove(x, y):
    """ randomly choose a direction
    1 = up, 2 = down, 3 = left, 4 = right"""
    direction =  # COMPLETE

    if direction == 1:  # move up
        y += 1
    elif direction == 2:  # move down
        y -= 1
    elif direction == 3:  # move right
        x += 1
    elif direction == 4:  # move left
        x -= 1
    else:
        print("error: direction isn't 1-4")

    return x, y


font = {'family': 'DejaVu Sans', 'size': 14}  # adjust fonts
rc('font', **font)

# %% main program starts here ------------------------------------------------|
# YOU NEED TO FINISH IT!

plt.ion()

Lp = 101  # size of domain
N = 100  # number of particles
# array to represent whether each gridpoint has an anchored particle
anchored = np.zeros((Lp, Lp), dtype=int)
# list to represent x and y positions of anchored points
anchored_points = [[], []]

centre_point = (Lp-1)//2  # middle point of domain

# set up animation of anchored points
plt.figure(1)
plt.title('DLA run for {} particles'.format(N))
plt.plot(centre_point, centre_point, '.r', markersize=10)
plt.xlim([-1, Lp])
plt.ylim([-1, Lp])
plt.xlabel('$x$ []')
plt.ylabel('$y$ []')

# set up animation of anchored points
animation_interval = 50  # how many moves to make before updating plot of

for j in range(N):
    xp = centre_point
    yp = centre_point
    i = 0  # counter to keep track of animation of moving particle

    # AND OFF YOU GO!
