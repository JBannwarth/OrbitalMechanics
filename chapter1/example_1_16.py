""" Orbital Mechanics for Engineering Students Example 1.16
Question:
Expand the function sin(t+h) in a Taylor series around t=1.
Plot the Taylor series of orders 1 to 4 and compare them with
sin(1+h) for -2<h<2.
Written by: J.X.J. Bannwarth
"""
import matplotlib.pyplot as plt
from sympy import symbols, diff, sin, cos
from math import factorial
from numpy import array, linspace, dot, zeros
import numpy as np

# Title
print("Orbital Mechanics for Engineering Students Example 1.16")

# Equation to approximate
t = symbols('t')
g = sin(t)

# Linearisation point
tLin = 1.

# Step size
hs = linspace(-2.,2.,50)
gTrue = np.sin(tLin + hs)

# Find the taylor coefficients
orders = range(5)
taylorCoefsEqn = [diff(g, t, order)/factorial(order) for order in orders]
taylorCoefs = array([coef.evalf(subs={t:tLin}) for coef in taylorCoefsEqn])

# Calculate the terms of the Taylor series polynomials
termApprox = zeros((hs.shape[0],len(orders)))
for idx, h in enumerate(hs):
    powers = array([h**order for order in orders])
    termApprox[idx,:] = powers * taylorCoefs

# Calculate the sum of the terms
gApprox = zeros((hs.shape[0],len(orders)))
gApprox[:,0] = termApprox[:,0]
for idx in range(1,gApprox.shape[1]):
    gApprox[:,idx] = termApprox[:,0:idx+1].sum(axis=1)

# Plot the results
plt.figure()
plt.grid()
plt.plot(hs, gTrue, label=f"sin(1+h)")
for idx, order in enumerate(orders):
    plt.plot(hs, gApprox[:,idx], label=f"$p_{order}$")
plt.xlabel("$h$ (-)")
plt.ylabel("Value (-)")
plt.title("Example 1.16 Plots of zeroth- to fourth-order\nTaylor series expansions of sin(1-h)")
plt.legend()
plt.show()
