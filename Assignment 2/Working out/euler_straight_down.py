# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67 * (10 ** (-11))
M = 6.42 * (10 ** (23))
m = 1
R = 3390*1000

# initial position
x = [3800*1000, 0, 0]
v = [0, 0 ,0]

# unit vector of displacement
mag_x = np.linalg.norm(x)
unit_x = x / mag_x

# dot unit position vecotr with each axis
dot_x = np.dot(unit_x, [1, 0 ,0])
dot_y = np.dot(unit_x, [0, 1, 0])
dot_z = np.dot(unit_x, [0, 0, 1])
dot_tuple = [dot_x, dot_y, dot_z]


# simulation time, timestep and time
t_max = 1000
dt = 1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
position = []
velocity = []
altitude = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    position.append(x)
    velocity.append(v)

    r = np.linalg.norm(x)
    altitude.append(r - R)

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
altitude_array = np.array(altitude)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, altitude_array, label='Altitude (m)')
plt.legend()
plt.show()
