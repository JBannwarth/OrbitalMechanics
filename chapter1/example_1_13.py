""" Orbital Mechanics for Engineering Students Example 1.13
Question:
Given:
    - Position, velocity, and acceleration of the origin O (RO,VO,AO)
    - Angular velocity and acceleration of moving frame (Omega, OmegaDot)
    - Unit vectors of the moving frame (iHat, jHat, kHat)
    - Absolute position, velocity, and acceleration of P (R,V,A)
Find:
    (a) The velocity Vrel of P relative to the moving frame
    (b) The acceleration Arel of P relative to the moving frame
Written by: J.X.J. Bannwarth
"""
from numpy import array, cross, dot, vstack
from numpy.linalg import inv

def PrintVec(v, name, unit = '', inertial=True):
    if inertial:
        print(f"{name} = {v[0]:.4f} I + {v[1]:.4f} J + {v[2]:.4f} K {unit}")
    else:
        print(f"{name} = {v[0]:.4f} i + {v[1]:.4f} j + {v[2]:.4f} k {unit}")

# Title
print("Orbital Mechanics for Engineering Students Example 1.13")

# Origin
RO = array([100.,200.,300.]) # m
VO = array([-50.,30.,-10.]) # m/s
AO = array([-15.,40.,25.]) # m/s^2

# Moving frame
Omega    = array([1.0,-0.4,0.6]) # rad/s
OmegaDot = array([-1.0,0.3,-0.4]) # rad/s^2

# Unit vectors
# <>Hat = x*IHat + y*JHat + z*KHat
iHat = array([0.5571,0.7428,0.3714])
jHat = array([-0.06331,0.4839,-0.8728])
kHat = array([-0.8280,0.4627,0.3166])

# Construct DCM from unit vectors
DCM = vstack((iHat,jHat,kHat))

# Absolute values
R = array([300.,-100.,150.]) # m
V = array([70.,25.,-20]) # m/s
A = array([7.5,-8.5,6.0]) # m/s^2

# (a)
print("Inertial frame: (I,J,K), moving frame: (i,j,k)")
print("(a)")
Rrel = R - RO
PrintVec(Rrel, "R_rel", "m")

Vrel = V - VO - cross(Omega,Rrel)
PrintVec(Vrel, "V_rel", "m/s")
PrintVec(dot(DCM,Vrel), "V_rel", "m/s", False)

# (b)
print("b")
Arel = A - AO - cross(OmegaDot,Rrel) - cross(Omega,cross(Omega,Rrel)) - 2*cross(Omega,Vrel)
PrintVec(Arel, "A_rel", "m/s^2")
PrintVec(dot(DCM,Arel), "A_rel", "m/s^2", False)
