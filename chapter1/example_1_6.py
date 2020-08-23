""" Orbital Mechanics for Engineering Students Example 1.6
Question:
Given the position, velocity, and acceleration of a particle P at a given
instant (R, V, A), find the coordinates of the center of curvature at that
instant.
Written by: J.X.J. Bannwarth
"""
from numpy import array, cross, dot
from numpy.linalg import norm

def PrintVec(v, name, unit = ''):
    print(f"{name} = {v[0]:.4f} i + {v[1]:.4f} j + {v[2]:.4f} k {unit}")

# Title
print("Orbital Mechanics for Engineering Students Example 1.6")

# Point P
R = array([250., 630., 430.])
V = array([90., 125., 170.])
A = array([16., 125., 30.])

# Tangential vector
Ut = V / norm(V)
PrintVec(Ut, "U_t")

# Binormal vector
Ub = cross(V,A) / norm(cross(V,A))
PrintVec(Ub, "U_b")

# Normal vector
Un = cross(Ub, Ut)
PrintVec(Un, "U_n")

# Normal acceleration
an = dot(A,Un)

# Radius of curvature
rho = norm(V)**2 / an
print(f"rho = {rho:.4f} m")

# Location of center of curvature
RCP = rho*Un
RC = R + RCP
print("Final answer:")
PrintVec(RC, "R_C", "m")