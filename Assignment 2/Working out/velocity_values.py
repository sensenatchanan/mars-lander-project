# calculate velocities for circular orbit and hyperbolic escape
import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67 * (10 ** (-11))
M = 6.42 * (10 ** (23))

# initial displacement from centre of planet
r = 3800 * 1000

# find and print orbital velocity
v_orbit = math.sqrt((G * M) / r)
print("Velocity for circular orbit is: ", round(v_orbit, 2), " m/s")

# find and print escape velocity
v_escape = math.sqrt((2 * G * M) / r)
print("Velocity for hyperbolic escape is: ", round(v_escape,2), " m/s")