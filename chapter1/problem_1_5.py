""" Orbital Mechanics for Engineering Students Problem 1.5
Question:

Written by: J.X.J. Bannwarth
"""
from numpy import array, dot, cross, sqrt, sin, cos, arccos, pi
from numpy.linalg import norm

# Function
def PrintVec(v, name, unit = '', inertial=True):
    if inertial:
        print(f"{name} = {v[0]:.4f} I + {v[1]:.4f} J + {v[2]:.4f} K {unit}")
    else:
        print(f"{name} = {v[0]:.4f} i + {v[1]:.4f} j + {v[2]:.4f} k {unit}")

# Title
print("Orbital Mechanics for Engineering Students Problem 1.5")

# Parameters
t = 3. # s

# Position
P = array([sin(3.*t), cos(t), sin(2.*t)])

print("(a)")
V = array([3.*cos(3.*t), -sin(t), 2.*cos(2.*t)])
PrintVec(V, "V", "m/s")

print("(b)")
v = norm(V)
print(f"v = {v} m/s")

print("(c)")
uT = V/v
PrintVec(uT, "u_t")

print("(d)")
th = arccos(V/v)*180./pi
print(f"th_x = {th[0]:.1f} deg, th_y = {th[1]:.1f} deg, th_z = {th[2]:.1f} deg")
