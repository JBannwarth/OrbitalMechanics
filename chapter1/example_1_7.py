""" Orbital Mechanics for Engineering Students Example 1.7
Question:
Show that if there is no atmosphere, the shape of a low-altitude ballistic
trajectory is a parabola. Assume the acceleration g is constant and neglect the
earth curvature
Written by: J.X.J. Bannwarth
"""
from numpy import linspace, tan, sin, cos, pi
import matplotlib.pyplot as plt

# Initial conditions
x0     = 1. # m
y0     = 1. # m
v0     = 5. # m/s
gamma0 = 60.*pi/180. # radian
g      = 9.807 # m/s^2
tmax = 2. # s

# Compute using y(t) for checking purposes
t = linspace(0.,tmax,20)
x = x0 + (v0*cos(gamma0))*t
y1 = y0 + (v0*sin(gamma0))*t - 0.5*g*t**2

# Compute using y(x)
y = y0 + (x-x0)*tan(gamma0) - 0.5*g*(x-x0)**2 / (v0*cos(gamma0))**2

# Plot trajectory
fig = plt.figure()
plt.grid()
plt.arrow(x0, y0, v0*cos(gamma0), v0*sin(gamma0), color='r', label="v0", head_width=0.2)
plt.plot(x, y, label="y(x)")
plt.plot(x, y1, '-.', label="y(t)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.ylim(top=y0+1.1*v0*sin(gamma0))
plt.show()
