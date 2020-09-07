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
from orbitutils.orbiting_bodies import two_body_3d, n_body_3d
import matplotlib.ticker

# Functions
def format_plot(ax, threeD=True):
    ax.set_xlabel("$X$ (km)")
    ax.set_ylabel("$Y$ (km)")
    if threeD:
        ax.set_zlabel("$Z$ (km)")
    # Label formatting
    mf = matplotlib.ticker.ScalarFormatter(useMathText=True)
    mf.set_powerlimits((-2, 2))
    ax.xaxis.set_major_formatter(mf)
    ax.yaxis.set_major_formatter(mf)
    if threeD:
        ax.zaxis.set_major_formatter(mf)
    ax.legend()


def plot_path(ax, R, color="red", name="$m$"):
    ax.plot(R[:, 0], R[:, 1], R[:, 2], color=color, label=f"Path of {name}")
    ax.scatter(R[(0, -1), (0, 0)], R[(0, -1), (1, 1)],
               R[(0, -1), (2, 2)], color=color, label=name)


def plot_path_2d(ax, R, color="red", name="$m$"):
    ax.plot(R[:, 0], R[:, 1], color=color, label=f"Path of {name}")
    ax.scatter(R[(0, -1), (0, 0)], R[(0, -1), (1, 1)], color=color, label=name)


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
y, t = two_body_3d(R1_0, R2_0, V1_0, V2_0, m1, m2, tSpan)
y = y / 1000.  # convert to km
R1 = y[:, 0:3]
R2 = y[:, 3:6]
G = (m1*R1 + m2*R2)/(m1+m2)

# (a) Motion of m1 and m2 relative to the inertial frame
figA = plt.figure("(a) Motion relative to inertial frame.")
axA = figA.add_subplot(111, projection="3d")
plot_path(axA, R1, color="red", name="$m_1$")
plot_path(axA, R2, color="green", name="$m_2$")
plot_path(axA, G, color="black", name="$G$")
axA.view_init(20, 30)
format_plot(axA)

plt.show()

# (b) Motion of m2 and G relative to m1
figB = plt.figure("(b) Motion relative to m1.")
axB = figB.add_subplot(111, projection="3d")
plot_path(axB, R2 - R1, color="green", name="$m_2$")
plot_path(axB, G - R1, color="black", name="$G$")
axB.view_init(20, 80)
format_plot(axB)

plt.show()

# (c) Motion of m1 and m2 relative to G
figC = plt.figure("(c) Motion relative to G.")
axC = figC.add_subplot(111, projection="3d")
plot_path(axC, R1 - G, color="red", name="$m_1$")
plot_path(axC, R2 - G, color="green", name="$m_2$")
axC.view_init(20, 80)
format_plot(axC)

plt.show()

# Bonus: 3-body problem
R_0 = np.array(
    [[0., 300000., 600000.],
     [0., 0., 0.],
     [0., 0., 0.]]
    ) * 1000.

V_0 = np.array(
    [[0., 250., 0.],
     [0., 250., 0.],
     [0., 0., 0.]]
    ) * 1000.

M = np.array([1.e29, 1.e29, 1.e29])
tSpanBonus = np.array([0., 67000.])

# Note: results obtained from solving using RKF45 diverge from those obtained
# using ODE45 as time increases (confirmed by using different RKF45
# implementations)
yBonus, tBonus = n_body_3d(R_0, V_0, M, tSpanBonus)
yBonus = yBonus/1000.

# Extract vectors of interest
R1Bonus = yBonus[:,0:3]
R2Bonus = yBonus[:,3:6]
R3Bonus = yBonus[:,6:9]

# Compute center of gravity
GBonus = (M[0]*R1Bonus + M[1]*R2Bonus + M[2]*R3Bonus) / np.sum(M)

# Plot output
fig = plt.figure("Bonus - 3 body problem wrt inertial")
axBonus = fig.add_subplot(111)
plot_path_2d(axBonus, GBonus , color="black", name="$G$")
plot_path_2d(axBonus, R1Bonus, color="red"  , name="$m_1$")
plot_path_2d(axBonus, R2Bonus, color="green", name="$m_2$")
plot_path_2d(axBonus, R3Bonus, color="blue" , name="$m_3$")
format_plot(axBonus, threeD=False)

plt.show()

fig = plt.figure("Bonus - 3 body problem wrt G")
axBonus = fig.add_subplot(111)
plot_path_2d(axBonus, R1Bonus - GBonus, color="red"  , name="$m_1$")
plot_path_2d(axBonus, R2Bonus - GBonus, color="green", name="$m_2$")
plot_path_2d(axBonus, R3Bonus - GBonus, color="blue" , name="$m_3$")
format_plot(axBonus, threeD=False)

plt.show()
