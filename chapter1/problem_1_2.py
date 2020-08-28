""" Orbital Mechanics for Engineering Students Problem 1.2
Question:
Given four vectors A, B, C, and D and the identities from Problem 1.1, show
    (A x B) . (C x D) = (A . C)(B . D) - (A . D)(B. C)
Written by: J.X.J. Bannwarth
"""
from sympy.vector import CoordSys3D
from sympy.vector import Vector
from sympy import symbols
from sympy import simplify

# Title
print("Orbital Mechanics for Engineering Students Problem 1.2")

# Coordinate system
N = CoordSys3D('N')
i, j, k = N.base_vectors()

# Define vectors
ax, ay, az = symbols("ax ay az")
bx, by, bz = symbols("bx by bz")
cx, cy, cz = symbols("cx cy cz")
dx, dy, dz = symbols("dx dy dz")
A = ax * i + ay * j + az * k
B = bx * i + by * j + bz * k
C = cx * i + cy * j + cz * k
D = dx * i + dy * j + dz * k

# Analytical
print("(1) Answer")
print("(A x B) . (C x D)")
print("A . [B x (C x D)] - interchangeability")
print("A . [C(B . D) - D(B . C)] - bac-cab")
print("(A . C)(B . D) - (A . D)(B . C) - expand")

# Check the equations work out
print("\n(2) Check")
LHS = simplify((A.cross(B)).dot(C.cross(D)))
RHS = simplify(A.dot(C) * B.dot(D) - A.dot(D) * B.dot(C))
print("(A x B) . (C x D) =", LHS)
print("(A . C)(B . D) - (A . D)(B . C) =", RHS)
if simplify(LHS - RHS) == 0:
    print("(A x B) . (C x D) == (A . C)(B . D) - (A . D)(B. C)")

