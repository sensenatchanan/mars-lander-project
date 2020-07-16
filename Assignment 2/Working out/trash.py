import numpy as np
import matplotlib.pyplot as plt

# declare constants
G = 6.67e-11
M = 6.42e23
R = 3389.5e3

# simulation time, timestep and time
t_max = 40000
dt = 0.1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
r_list = []
v_list = []

#declare position and velocity vectors
x0= 0
y0 = 10000e3
z0= 0
vx0 = np.sqrt(G*M/y0)
vy0 =0
vz0 = 0


# create lists
position = [[x0, y0, z0]]
velocity = [[vx0, vy0, vz0]]


print('start')
# integration function
p = [x0+vx0*dt, y0+vy0*dt, z0+vz0*dt]
v = [vx0, vy0, vz0]


# Verlet integration
for t in t_array:

    r_mag = np.linalg.norm(p)
    a = (G * M) / (r_mag**2)

    position.append(p[i] for i in range(3))
    velocity.append(v[i] for i in range(3))

    for i in range(3):
        p[i] = (2*p[i]) - ((dt**2) * a * p[i]) - (position[-2][i])
        v[i] = (p[i] - (position[-2][i])) / (2*dt)

    
# convert trajectory lists into arrays, so they can be sliced
r_array = np.array(r_list)
v_array = np.array(v_list)


print(r_array)
print(v_array)


#plot the trajectory against time
plt.figure(2)
plt.clf()
plt.xlabel('time (s)')
plt.ylabel('distance from centre (m)')
plt.grid()
plt.plot(t_array, r_array[:,0], label='x values')
plt.plot(t_array, r_array[:,1], label='y values')
plt.plot(t_array, r_array[:,2], label='z values')
plt.legend()
plt.show()

#plot orbit
plt.figure(2)
plt.clf()
plt.xlabel('x distance (m)')
plt.ylabel('y distance (m)')
plt.grid()
plt.plot(r_array[:,0], r_array[:,1], label='orbit')
plt.legend()
plt.show()
