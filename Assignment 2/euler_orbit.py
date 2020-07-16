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

# initialise empty lists to record trajectories
position = []
velocity = []

#declare position and velocity vectors
x = 0
y = 10000e3
z = 0
# circular orbit velocity np.sqrt(G*M/y)
# eliptial orbit velocity np.sqrt(1.5*G*M/y)
# hyperbolic escape velocity np.sqrt(2*G*M/y)
vx = np.sqrt(G*M/y)
vy = 0
vz = 0

p = np.array([x,y,z])
v = np.array([vx,vy,vz])


# integration function
for t in t_array:

    # magnitude of position vector
    p_mag = np.linalg.norm(p) 

    if p_mag > R:
        
        # append current state to trajectories
        position.append(p)
        velocity.append(v)

        # scalar acceleration, new position and velocity values
        a = G * M / (p_mag**3) 
        v = v - a * p *dt
        p = p + v * dt

    else:
        position.append(p)
        velocity.append(v)
        p = R
        v = 0
        

    
# convert trajectory lists into arrays, so they can be sliced
p_array = np.array(position)
v_array = np.array(velocity)



# plot the trajectory against time
plt.figure(2)
plt.clf()
plt.xlabel('Time (s)')
plt.ylabel('Distance from centre (datum) (m)')
plt.grid()
plt.plot(t_array, p_array[:,0], label='X axis')
plt.plot(t_array, p_array[:,1], label='Y axis')
plt.plot(t_array, p_array[:,2], label='Z axis')
plt.legend()
plt.show()

# plot orbit
plt.figure(2)
plt.clf()
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid()
plt.plot(p_array[:,0], p_array[:,1], label='Trajectory')
plt.legend()
plt.show()
