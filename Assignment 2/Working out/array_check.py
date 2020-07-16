# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67 * (10 ** (-11))
M = 6.42 * (10 ** (23))
m = 1
R = 30000

# initial position
x = [400*1000, 200*1000, 0]

# unit vector of displacement
mag_x = np.linalg.norm(x)
unit_x = x / mag_x

# initial velocity
v_mag = 1
v = np.cross(unit_x, [0,0,1]) * v_mag

# dot unit position vecotr with each axis
dot_x = np.dot(unit_x, [1, 0 ,0])
dot_y = np.dot(unit_x, [0, 1, 0])
dot_z = np.dot(unit_x, [0, 0, 1])
dot_tuple = [dot_x, dot_y, dot_z]


# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
position = []
velocity = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    position.append(x)
    velocity.append(v)

    r = np.linalg.norm(x)

    # calculate new position and velocity
    if (r < R):
        x = x
        v = [0, 0, 0]
    else:
         for i in range(3):
            a = - (G * M) / (r**2)
            a *= dot_tuple[i]
            x[i] = x[i] + dt * v[i]
            v[i] = v[i] + dt * a

    x = [x[0], x[1], x[2]]




# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
position_array = np.array(position)
velocity_array = np.array(velocity)

print(position_array)

# plot the position-time graph
for i in range(int(t_max/dt)):
    print(position_array[i][0])
    if i > 0:
        print("previous", position_array[i-1][0])
    else:
        print("no previous")