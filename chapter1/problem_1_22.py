""" Orbital Mechanics for Engineering Students Problem 1.22
Question:
Numerically determine how long it would take for the moon to fall to the earth
if it was stopped in its orbit and the earth was fixed in space.
Use the 'shooting method' (estimate an end-time and manually adjust until it is
large enough for the moon to reach the earth).
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt
from numerical_solvers import SolveRKF45, SolveRK14
import datetime


# Differential equations
def Rates(t, Y):
    g0 = 9.80665
    RE = 6378.E3
    F = np.zeros(Y.shape)
    F[0] = Y[1]
    F[1] = - g0*RE**2/Y[0]**2.
    return F


# Title
print("Orbital Mechanics for Engineering Students Problem 1.22")

# Parameters
RE = 6378.E3  # m, radius earth
RM = 1737.E3  # m, radius moon
r0 = 384.4E6  # m, moon orbit
tSpan = np.array([0., 418850.])
Y0 = np.array([r0, 0.])

# Solve numerically
y, t = SolveRKF45(Rates, Y0, tSpan)
r = y[:, 0]

# Find time for the surface of the moon to reach the surface of the earth
tEnd = np.interp(RE+RM, np.flip(r), np.flip(t))
timeStr = str(datetime.timedelta(seconds=tEnd))

# Analytical answer
g0 = 9.80665
r1 = RE+RM
tAnalytical = np.sqrt(r0/(2.*g0*RE**2))*(np.pi*r0/4. +
                                         np.sqrt(r1*(r0-r1)) + 0.5*r0*np.arcsin((r0-2*r1)/r0))
timeStrAnalytical = str(datetime.timedelta(seconds=tAnalytical))

# Show answer
print(f"Numercial ime to reach the surface of the earth = {timeStr} ")
print(
    f"Analytical time to reach the surface of the earth = {timeStrAnalytical} ")
print(f"Accuracy: {tAnalytical-tEnd:.4f} s")

# Plot answer
plt.figure()
plt.plot(t, r/1.E3)
plt.plot([t[0], t[-1]], (RE+RM)*np.ones((2,))/1.E3, label="$R_E+R_M$")
plt.xlabel("Time (s)")
plt.ylabel("Radius to moon (km)")
plt.legend()
plt.show()
