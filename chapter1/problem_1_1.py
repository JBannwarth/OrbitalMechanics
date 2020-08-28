""" Orbital Mechanics for Engineering Students Problem 1.1
Question:
Given three vectors A, B, and C, prove analytically that:
    (a) A . A = |A|**2
    (b) A . (B x C) = (A x B) . C
    (c) A x (B x C) = B(A . C) - C(A . B)
Written by: J.X.J. Bannwarth
"""
from sympy.vector import CoordSys3D
from sympy.vector import Vector
from sympy import symbols
from sympy import simplify


# Function
def AreEqual(A, B):
    return simplify(A - B).equals(Vector.zero)


# Title
print("Orbital Mechanics for Engineering Students Problem 1.1")

# Coordinate system
N = CoordSys3D('N')
i, j, k = N.base_vectors()

# Define vectors
ax, ay, az = symbols("ax ay az")
bx, by, bz = symbols("bx by bz")
cx, cy, cz = symbols("cx cy cz")
A = ax * i + ay * j + az * k
B = bx * i + by * j + bz * k
C = cx * i + cy * j + cz * k

# (a)
print("(a)")
print("A . A =", A.dot(A))
print("|A|**2 = ", A.magnitude()**2)

# (b)
print("\n(b)")
bLHS = A.dot(B.cross(C))
bRHS = (A.cross(B)).dot(C)

print("A . (B x C) = ", bLHS)
print("(A x B) . C = ", bRHS)
if simplify(bLHS - bRHS) == 0:
    print("A . (B x C) == (A x B) . C")

# (c)
print("\n(c)")
cLHS = simplify(A.cross(B.cross(C)))
cRHS = simplify(B * A.dot(C) - C * A.dot(B))

print("A x (B x C) = ", cLHS)
print("B(A . C) - C(A . B) = ", cRHS)
if AreEqual(cLHS, cRHS):
    print("A x (B x C) == B(A . C) - C(A . B)")

