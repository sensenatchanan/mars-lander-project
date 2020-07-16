import numpy as np
import matplotlib.pyplot as plt
import math

# constants
G = 6.67e-11
M = 6.42e23
R = 3389.5e3

# simulation time, timestep and time
t_max = 10000
dt = 1
t_array = np.arange(0, t_max, dt)


# declare position and velocity vectors
x= 0
y = 10000e3
z = 0
# circular orbit velocity np.sqrt(G*M/y)
# eliptial orbit velocity np.sqrt(1.5*G*M/y)
# hyperbolic escape velocity np.sqrt(2*G*M/y)
vx = 0
vy = 0
vz = 0

# initialise empty lists and second values
position = [[x, y, z]]
velocity = [[vx, vy, vz]]
altitude = []

alt0 = math.sqrt(x**2 + y**2 + z**2) - R
altitude.append(alt0)

p = np.array([x + vx*dt, y+ vy*dt, z + vz*dt])
v = np.array([vx, vy, vz])


# vertlet function
for t in t_array:

    # magnitude of position vector
    p_mag = np.linalg.norm(p) 
    altitude.append(p_mag - R)

    if p_mag > R:
        
        # append current state to trajectories
        position.append(p)
        velocity.append(v)

        # scalar acceleration, new position and velocity values
        a = G*M / (p_mag**3) 

        p = 2*p - position[-2] - dt**2 * a*p
        v = (p - position[-1]) / dt
    
    else:
        position.append(p)
        velocity.append(v)

        p = R
        v = 0

        
del position[-1]
del velocity[-1]
del altitude[-1]
    
# convert trajectory lists into arrays, so they can be sliced
p_array = np.array(position)
v_array = np.array(velocity)


# plot altitude
plt.figure(2)
plt.clf()
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.grid()
plt.plot(t_array, altitude)
plt.legend()
plt.show()
