import numpy as np
import matplotlib.pyplot as plt
import math

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
position_list = [[400,300,0]]
velocity_list = [[0 ,0 ,0]]



# simulation time, timestep and time
t_max = 100
dt = 1
t_array = np.arange(0, t_max, dt)

# create altitude list
altitude_list = []

n = 0

x = position_list[n][0]
y = position_list[n][1]
z = position_list[n][2]
vx = velocity_list[n][0]
vy = velocity_list[n][1]
vz = velocity_list[n][2]

r = math.sqrt(position_list[n][0]**2 + position_list[n][1]**2 + position_list[n][2]**2)
print (r)