""" Orbital Mechanics for Engineering Students Example 1.17
Question:
Plot
    xDDot + 2*zeta*omegaN*xDot + omegaN**2*x = F0/m*sin(omega*t)
from t = 0 to t = 110 s using the exact solution.
Parameter values:
    - m = 1 kg
    - omegaN = 1 rad/s
    - zeta = 0.03
    - F0 = 1 N
    - omega = 0.4 rad/s
Initial conditions:
    x = xDot = 0
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt


# Exact response - Equations (1.114a) and (1.114b)
# Note: there is a mistake in the textbook, the denominator of the second term
# of (1.114a) should end with (2*w*wN*z)**2 rather than just (2*w*wN*z)
def CartSystemExactResponse(t, Y0, m=1.0, wN=1.0, z=0.03, f0=1.0, w=0.4):
    # Initial states
    x0 = Y0[0]
    xDot0 = Y0[1]

    # Damped natural frequency
    wD = wN * np.sqrt(1 - z**2)

    # Coefficients
    a = z * (wN / wD) * x0 + xDot0 / wD + (
        (w**2 + (2 * z**2 - 1) * wN**2) * w * f0) / ((
            (wN**2 - w**2)**2 + (2 * w * wN * z)**2) * wD * m)
    b = x0 + ((2 * w * wN * z) * f0) / ((
        (wN**2 - w**2)**2 + (2 * w * wN * z)**2) * m)

    x = np.exp(-z * wN * t) * (a * np.sin(wD * t) + b * np.cos(wD * t)) + (
        (wN**2 - w**2) * np.sin(w * t) - 2 * w * wN * z * np.cos(w * t)) * (
            f0 / m) / ((wN**2 - w**2)**2 + (2 * w * wN * z)**2)
    return x


# Answer - Equation (1.115)
def Answer(t, m=1.0, omegaN=1.0, zeta=0.03, F0=1.0, omega=0.4):
    x = np.exp(-0.03 * t) * (
        0.03399 * np.cos(0.9995 * t) - 0.4750 * np.sin(0.9995 * t)) + (
            1.190 * np.sin(0.4 * t) - 0.03399 * np.cos(0.4 * t))
    return x

# Title
print("Orbital Mechanics for Engineering Students Example 1.17")

# Get response
t = np.linspace(0., 110., 500)
Y0 = [0, 0]
xExact = CartSystemExactResponse(t, Y0)
xAnswer = Answer(t)

# Plot results
fig = plt.figure()
plt.grid()
plt.plot(t, xExact, label="Exact")
plt.plot(t, xAnswer, "--", label="Answer")
plt.xlabel("$t$ (s)")
plt.ylabel("$x$ (m)")
plt.legend()
plt.xlim((0, 110))
plt.ylim((-2, 2))
plt.tight_layout()
plt.show()

