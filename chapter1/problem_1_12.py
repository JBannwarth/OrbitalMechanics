""" Orbital Mechanics for Engineering Students Problem 1.12
Question:
Find the absolute velocity and acceleration of P in the inertial frame XYZ
given the provided information (refer to textbook for full question).
Written by: J.X.J. Bannwarth
"""
from numpy import array, cross, dot, vstack
from numpy.linalg import norm
from utilities import PrintVec

# Provided information
# Position, velocity and acceleration of O expressed in XYZ
R0 = array([-16.,84.,59.]) # m
V0 = array([7.,9.,4.])     # m/s
A0 = array([3.,-7.,4.])    # m/s^2

# Angular velocity and acceleration of moving frame in XYZ
W = array([-0.8,0.7,0.4])     # rad/s
WDot = array([-0.4,0.9,-1.0]) # rad/s^2

# Unit vectors of moving frame in XYZ
iHat = array([-0.15670,-0.31235,0.93704])
jHat = array([-0.12940,0.94698,0.29409])
kHat = array([-0.97922,-0.075324,-0.18831])

# Absolute position of P in XYZ
R = array([51.,-45.,36.])

# Velocity and acceleration of P relative to moving frame in xyz
VRel = array([31.,-68.,-77.])
ARel = array([2.,-6.,5.])

# Answer
# Title
print("Orbital Mechanics for Engineering Students Problem 1.12")

# Construct DCM to go from XYZ to xyz using unit vectors
DCM = vstack((iHat,jHat,kHat))

# Calculate velocity
# Do the computation in XYZ, gives the same result as doing it in xyz
# and converting after
V = V0 + cross(W, R-R0) + dot(DCM.T,VRel)
print(f"V_p = {norm(V):.1f} u_v m/s")
PrintVec(V/norm(V), "u_v", big=True)

# Calculate acceleration
A = A0 + cross(WDot, R-R0) + cross(W, cross(W,R-R0)) + 2*cross(W,dot(DCM.T,VRel)) + dot(DCM.T,ARel)
print(f"A_p = {norm(A):.1f} u_a m/s^2")
PrintVec(A/norm(A), "u_a", big=True)
