""" Orbital Mechanics for Engineering Students Example 2.2
Question:
    Two bodies of mass m1 = m2 = 10**26 have the following states at t=0 s:
        R1_0 = 0
        R2_0 = 3000*I km
        V1_0 = 10*I + 20*J + 30*K km/s
        V2_0 = 40*J (km/s)
    Solve the motion of the masses from t=0 to t=480 s.
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utilities import TwoBody3D
import matplotlib.ticker

# Title
print("Orbital Mechanics for Engineering Students Example 2.2")

# Constants
R1_0 = np.zeros((3,)) * 1000.
R2_0 = np.array([3000., 0., 0.]) * 1000.
V1_0 = np.array([10., 20., 30.]) * 1000.
V2_0 = np.array([0., 40., 0.]) * 1000.
m1 = 10.**26
m2 = 10.**26
tSpan = np.array([0., 480.])

# Solve the problem
y, t = TwoBody3D(R1_0, V1_0, R2_0, V2_0, tSpan, m1, m2)
y = y / 1000. # convert to km
R1 = y[:,0:3]
R2 = y[:,3:6]
G = (m1*R1 + m2*R2)/(m1+m2)

# Measurements relative to m1
R1m1 = R1 - R1
R2m1 = R2 - R1
Gm1 = G - R1

# Measurements relative to G
R1G = R1 - G
R2G = R2 - G

# (a) Motion of m1 and m2 relative to the inertial frame
figA = plt.figure("(a) Motion relative to inertial frame.")
axA = figA.add_subplot(111, projection="3d")
axA.plot(R1[:,0],R1[:,1],R1[:,2], color="red", label='Path of $m_1$')
axA.scatter(R1[(0,-1),(0,0)],R1[(0,-1),(1,1)],R1[(0,-1),(2,2)], color="red", label='$m_1$')
axA.plot(R2[:,0],R2[:,1],R2[:,2], color="green", label='Path of $m_2$')
axA.scatter(R2[(0,-1),(0,0)],R2[(0,-1),(1,1)],R2[(0,-1),(2,2)], color="green", label='$m_2$')
axA.plot(G[:,0],G[:,1],G[:,2], color="black", label='Path of $G$')
axA.scatter(G[(0,-1),(0,0)],G[(0,-1),(1,1)],G[(0,-1),(2,2)], color="black", label='$m_2$')
axA.view_init(20,30)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_zlabel("$Z$")
# Label formatting
mf = matplotlib.ticker.ScalarFormatter(useMathText=True)
mf.set_powerlimits((-2,2))
axA.xaxis.set_major_formatter(mf)
axA.yaxis.set_major_formatter(mf)
axA.zaxis.set_major_formatter(mf)

axA.legend()
plt.show()

# (b) Motion of m2 and G relative to m1
figA = plt.figure("(b) Motion relative to m1.")
axA = figA.add_subplot(111, projection="3d")
axA.plot(R2m1[:,0],R2m1[:,1],R2m1[:,2], color="green", label='Path of $m_2$')
axA.scatter(R2m1[0,0],R2m1[0,1],R2m1[0,2], color="green", label='$m_2$')
axA.plot(Gm1[:,0],Gm1[:,1],Gm1[:,2], color="black", label='Path of $G$')
axA.scatter(Gm1[(0,-1),(0,0)],Gm1[(0,-1),(1,1)],Gm1[(0,-1),(2,2)], color="black", label='$m_2$')
axA.view_init(20,80)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_zlabel("$Z$")
# Label formatting
mf = matplotlib.ticker.ScalarFormatter(useMathText=True)
mf.set_powerlimits((-2,2))
axA.xaxis.set_major_formatter(mf)
axA.yaxis.set_major_formatter(mf)
axA.zaxis.set_major_formatter(mf)
axA.legend()
plt.show()

# (b) Motion of m1 and m2 relative to G
figA = plt.figure("(b) Motion relative to G.")
axA = figA.add_subplot(111, projection="3d")
axA.plot(R1G[:,0],R1G[:,1],R1G[:,2], color="red", label='Path of $m_1$')
axA.scatter(R1G[(0,-1),(0,0)],R1G[(0,-1),(1,1)],R1G[(0,-1),(2,2)], color="red", label='$m_1$')
axA.plot(R2G[:,0],R2G[:,1],R2G[:,2], color="green", label='Path of $m_2$')
axA.scatter(R2G[0,0],R2G[0,1],R2m1[0,2], color="green", label='$m_2$')
axA.view_init(20,80)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_zlabel("$Z$")
# Label formatting
mf = matplotlib.ticker.ScalarFormatter(useMathText=True)
mf.set_powerlimits((-2,2))
axA.xaxis.set_major_formatter(mf)
axA.yaxis.set_major_formatter(mf)
axA.zaxis.set_major_formatter(mf)
axA.legend()
plt.show()

print("Done")
