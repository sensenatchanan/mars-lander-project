# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67 * (10 ** (-11))
M = 6.42 * (10 ** (23))
m = 1

# initial position
x = [400*1000, 200*1000, 0]
v = [0, 0 ,0]

# unit vector
mag_x = np.linalg.norm(x)
unit_x = x / mag_x
print(unit_x)

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
altitude = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    position.append(x)
    velocity.append(v)

    r = np.linalg.norm(x)
    altitude.append(r)

    # calculate new position and velocity
    if (r < 30000):
        x = x
        v = [0, 0, 0]
    else:
         for i in range(3):
            a = - (G * M) / (r**2)
            a *= dot_tuple[i]
            x[i] = x[i] + dt * v[i]
            v[i] = v[i] + dt * a

    x = [x[0], x[1], x[2]]


print (altitude)


# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
position_array = np.array(position)
velocity_array = np.array(velocity)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, position_array, label='x (m)')
plt.legend()
plt.show()
