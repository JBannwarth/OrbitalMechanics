""" Orbital Mechanics for Engineering Students Problem 1.11
Question:
Find the third derivative of the fixed-magnitude vector F, given
    Omega = 2 k rad/s
    OmegaDot = -5 k rad/s^2
    OmegaDDot = 3 k rad/s^3
    F = 15 i + 10 j N.
Written by: J.X.J. Bannwarth
"""
from numpy import array, cross
from utilities import PrintVec

# Variables
W     = array([0.,0.,2.])  # rad/s
WDot  = array([0.,0.,-5.]) # rad/s^2
WDDot = array([0.,0.,3.])  # rad/s^3
F     = array([15.,10.,0]) # N

# Title
print("Orbital Mechanics for Engineering Students Problem 1.11")

# Find answer
FDDDot = cross(WDDot, F) + 2.*cross(WDot, cross(W,F)) + cross(W, (cross(WDot,F) + cross(W,cross(W,F))))
PrintVec(FDDDot, 'FDDDot', 'N/s^3')
