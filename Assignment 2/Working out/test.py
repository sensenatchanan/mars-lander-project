# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67 * (10 ** (-11))
M = 6.42 * (10 ** (23))
R = 3390 * 1000

# initial position
x = [3800*1000, 0, 0]

# unit vector of displacement
mag_x = np.linalg.norm(x)
unit_x = x / mag_x

# initial velocity
v0_mag = 3400
v0 = np.cross(unit_x, [0,0,1]) * v_mag
print (v)


# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)

# create iterated values
p = [x+(vx*dt), y+(vy*dt), z+(v[2]*dt)]
v = [v[0], [v[1], x[2]]



# Verlet integration
for t in t_array:

    r = np.linalg.norm(p)
    a = (G * M) / (r**2)

    position.append(p[i] for i in range(3))
    velocity.append(v[i] for i in range(3))

    if r > R:
        for i in range(3):
            p[i] = (2*p[i]) - ((dt**2) * a * p[i]) - (position[-2][i])
            v[i] = (p[i] - (position[-2][i])) / (2*dt)



# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(position)
v_array = np.array(velocity)



# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(x_array, alt_array, label='Altitude (m)')
plt.legend()
plt.show()
