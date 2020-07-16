import numpy as np
import matplotlib.pyplot as plt

# constants
G = 6.67e-11
M = 6.42e23
R = 3389.5e3

# simulation time, timestep and time
t_max = 100000
dt = 1
t_array = np.arange(0, t_max, dt)


# declare position and velocity vectors
x= 0
y = 10000e3
z = 0
# circular orbit velocity np.sqrt(G*M/y)
# eliptial orbit velocity np.sqrt(1.5*G*M/y)
# hyperbolic escape velocity np.sqrt(2*G*M/y)
vx = np.sqrt(1.5*G*M/y)
vy = 0
vz = 0

# initialise empty lists and second values
position = [[x, y, z]]
velocity = [[vx, vy, vz]]

p = np.array([x + vx*dt, y+ vy*dt, z + vz*dt])
v = np.array([vx, vy, vz])


# vertlet function
for t in t_array:

    # magnitude of position vector
    p_mag = np.linalg.norm(p) 

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
    
# convert trajectory lists into arrays, so they can be sliced
p_array = np.array(position)
v_array = np.array(velocity)



# plot the trajectory against time
plt.figure(2)
plt.clf()
plt.xlabel('Time (s)')
plt.ylabel('Distance from centre (datum) (m)')
plt.grid()
plt.plot(t_array, p_array[:,0], label='X Axis')
plt.plot(t_array, p_array[:,1], label='Y Axis')
plt.plot(t_array, p_array[:,2], label='Z Axis')
plt.legend()
plt.show()

# plot orbit
plt.figure(2)
plt.clf()
plt.xlabel('x distance (m)')
plt.ylabel('y distance (m)')
plt.grid()
plt.plot(p_array[:,0], p_array[:,1], label='Trajectory')
plt.legend()
plt.show()
