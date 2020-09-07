""" Orbital Mechanics for Engineering Students Example 1.20
Question:
    A spacecraft S of mass m travels in a straight line away from the center
    of the earth C. If at 6500 km from C, its outbound velocity is 7.8km/s,
    what will be its position and velocity 70 minutes later?
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt
from orbitutils.solvers import rkf45
import matplotlib.ticker


# Differential equations
def SpacecraftRates(t, y):
    g0 = 9.807  # m/s^2
    rE = 6378000  # m/s^2

    f = np.zeros((2,))
    f[0] = y[1]
    f[1] = - g0*rE**2/y[0]**2
    return f


# Title
print("Orbital Mechanics for Engineering Students Example 1.20")

# Parameters
tSpan = np.array([0, 70.*60.])
Y0 = np.array([6500000., 7800.])

y, t = rkf45(SpacecraftRates, Y0, tSpan)

# Plot results - Fig. 1.26
fig, ax = plt.subplots(2)
# Position
ax[0].grid()
ax[0].plot(t/60., y[:, 0]/1000., "o-", color="black",
           markerfacecolor='none', label=f"RKF")
ax[0].set_xlabel("Time (min)")
ax[0].set_ylabel("Position (km)")
ax[0].set_xlim((0., 70.))
ax[0].set_ylim((0.5e4, 1.5e4))
mf = matplotlib.ticker.ScalarFormatter(useMathText=True)
mf.set_powerlimits((-1,1))
ax[0].yaxis.set_major_formatter(mf)
ax[0].set_yticks(ticks=[0.5e4,1e4,1.5e4])

# Velocity
ax[1].grid()
ax[1].plot(t/60., y[:, 1]/1000., "o-", color="black",
           markerfacecolor='none', label=f"RKF")
ax[1].set_xlabel("Time (min)")
ax[1].set_ylabel("Velocity (km/s)")
ax[1].set_xlim((0., 70.))
ax[1].set_ylim((-10., 10.))

plt.tight_layout()
plt.show()
