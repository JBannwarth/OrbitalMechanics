""" Orbital Mechanics for Engineering Students Problem 1.5
Question:
Given the particle
    P = sin(3t) i + cos(t) j + sin(2t) k
find the velocity, acceleration, angles that the velocity and acceleration
vectors make with the inertial frame, and the location of the centre of
curvature of the path.
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

# Answers
print("(a)")
V = array([3.*cos(3.*t), -sin(t), 2.*cos(2.*t)])
PrintVec(V, "V", "m/s")

print("(b)")
v = norm(V)
print(f"v = {v:.3f} m/s")

print("(c)")
uT = V/v
PrintVec(uT, "u_t")

print("(d)")
th = arccos(V/v)*180./pi
print(f"th_x = {th[0]:.1f} deg, th_y = {th[1]:.1f} deg, th_z = {th[2]:.1f} deg")

print("(e)")
A = array([-9.*sin(3.*t), -cos(t), -4.*sin(2.*t)])
PrintVec(A, "A", "m/s^2")

print("(f)")
uB = cross(V,A)/norm(cross(V,A))
PrintVec(uB, "u_b")

print("(g)")
uN = cross(uB, uT)
PrintVec(uN, "u_n")

print("h")
a = norm(A)
ph = arccos(A/a)*180./pi
print(f"ph_x = {ph[0]:.1f} deg, ph_y = {ph[1]:.1f} deg, ph_z = {ph[2]:.1f} deg")

print("(i)")
aT = dot(A, uT)
print(f"a_t = {aT:.3f} m/s^2")

print("(j)")
aN = dot(A, uN)
print(f"a_n = {aN:.3f} m/s^2")

print("(k)")
rho = v**2/aN
print(f"rho = {rho:.3f} m/s^2")

print("(l)")
RCP = rho*uN
C = P + RCP
PrintVec(C, "C", "m")
