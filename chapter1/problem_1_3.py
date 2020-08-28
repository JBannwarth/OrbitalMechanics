""" Orbital Mechanics for Engineering Students Problem 1.3
Question:
Given
    A = 8*i + 9*j + 12*k
    B = 9*i + 6*j + k
    C = 3*i + 5*j + 10*k
Calculate the projection of C, cAB, on the plane of A and B.
Written by: J.X.J. Bannwarth
"""
from numpy import array, dot, cross, sqrt
from numpy.linalg import norm

# Title
print("Orbital Mechanics for Engineering Students Problem 1.3")

# Vectors
A = array([8., 9., 12.])
B = array([9., 6., 1.])
C = array([3., 5., 10.])

# Unit normal to AB plane
uN = cross(A, B) / norm(cross(A, B))

# Projection of C on uN
cN = dot(C, uN)

# Projection of C on AB plane
cAB = sqrt(norm(C)**2 - cN**2)
print(f"c_AB = {cAB:.2f}")

