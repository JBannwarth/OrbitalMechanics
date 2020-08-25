""" Orbital Mechanics for Engineering Students Example 1.14
Question:
A 70,000 kg airplane travels north at a latitude of 30 deg N, at an altitude of 10 km, with a speed of 300 m/s.
Find:
    (a) The components of the absolute velocity (V) and acceleration (A) along the axes of the topocentric-horizon reference frame.
    (b) The net force on the airplane.
Assumption:
	- Winds aloft are zero.
Written by: J.X.J. Bannwarth
"""
from numpy import array, pi, cos, sin
from numpy.linalg import norm


def PrintVec(v, name, unit = '', inertial=True):
    if inertial:
        print(f"{name} = {v[0]:,.4f} I + {v[1]:,.4f} J + {v[2]:,.4f} K {unit}")
    else:
        print(f"{name} = {v[0]:,.4f} i + {v[1]:,.4f} j + {v[2]:,.4f} k {unit}")

# Title
print("Orbital Mechanics for Engineering Students Example 1.14")

# Variables
mAirplane = 70000. # kg
vNorth = 300. # m/s
latitude = 30.*pi/180. # rad
z = 30000. # m
rE = 6378000. # m
siderealE = 23.9345*3600. # s for each revolution

# (a)
print("(a)")
omegaE = 2.*pi/siderealE

# Equations for flight due north at constant speed and altitude (zDot = zDDot = xDot = xDDot = yDDot = 0)
yDot = vNorth
phi = latitude
V = array([omegaE*(rE + z)*cos(phi),yDot,0.])
PrintVec(V, "V", "m/s", False)

A = array([ -2.*omegaE*yDot*sin(phi),
             omegaE**2.*(rE+z)*sin(phi)*cos(phi),
            -(yDot**2./(rE+z) + omegaE**2.*(rE+z)*cos(phi)**2.) ])
PrintVec(A, "A", "m/s^2", False)

# (b)
print("(b)")

Fnet = mAirplane*A
f = norm(Fnet)
PrintVec(Fnet, "F_net", "N", False)

# Force in the z-direction is a combination of the lift and the weight
g = 9.807/(1.+z/rE)**2.
wAirplane = g*mAirplane
L = wAirplane + Fnet[2]
reduction = 100.*(wAirplane-L)/wAirplane
print(f"Weight airplane = {wAirplane:,.2f} N, Lift = {L:,.2f} N")
print(f"Lift reduction due to rotation = {reduction:.2f}%")

