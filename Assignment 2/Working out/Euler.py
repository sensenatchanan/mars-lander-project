# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67 * (10 ** (-11))
M = 6.42 * (10 ** (23))
m = 1

# initial position
position_list = [[30000,0,0]]
velocity_list = [[0 ,0 ,0]]



# simulation time, timestep and time
t_max = 140
dt = 1
t_array = np.arange(0, t_max, dt)

# create altitude list
altitude_list = []

n = 0

# Euler integration
for t in t_array:

    # declare variables
    x = position_list[n][0]
    y = position_list[n][1]
    z = position_list[n][2]
    vx = velocity_list[n][0]
    vy = velocity_list[n][1]
    vz = velocity_list[n][2]

    # calculate new position and velocity
    r = math.sqrt(position_list[n][0]**2 + position_list[n][1]**2 + position_list[n][2]**2)


    a = - G * M / (r**3)
    x = x + dt * vx
    y = y + dt * vy
    z = z + dt * vz
    vx = vx + dt * a

    


    # append current state to trajectories
    position_list.append([x , y , z])
    velocity_list.append([vx, vy , vz])
    altitude_list.append(r)

    n = n + 1

# convert altitude lists into arrays, so they can be sliced
altitude_array = np.array(altitude_list)

print (altitude_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, altitude_array, label='Altitude (m)')
plt.legend()
plt.show()
