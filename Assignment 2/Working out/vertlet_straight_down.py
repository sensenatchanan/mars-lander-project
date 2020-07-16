# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67 * (10 ** (-11))
M = 6.42 * (10 ** (23))
R = 3390 * 1000

# inital state
x1 = 3400*1000
v1 = 0

# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, (t_max - dt), dt)
t_graph_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
position = []
velocity = []
altitude = []

# append initial values 
position.append(x1)
velocity.append(v1)

# set second values using Euler
a = - (G * M ) / (x1**2)
x2 = x1 + dt * v1
v2 = v1 + dt * a

# make a copy of current values as version 3
x3 = x2
v3 = v2


# Verlet integration
for t in t_array:

    # append current state to trajectories
    position.append(x3)
    velocity.append(v3)

    r = abs(x3)
    altitude.append(r-R)

    if (r > R):
        # calculate new position and velocity
        a = - (G * M ) / (x3 ** 2)
        x3 = (2 * x2) - x1 + (dt*dt) * a
        v3 = (x3 - x1)/(2*dt)

        # shift current value to previous
        x1 = x2
        x2 = x3

        v1 = v2
        v2 = v3
    else:
        x3 = R
        v3 = 0



# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(position)
v_array = np.array(velocity)
alt_array = np.array(altitude)


# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, alt_array, label='Altitude (m)')
plt.legend()
plt.show()
