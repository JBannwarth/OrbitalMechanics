""" Orbital Mechanics for Engineering Students Example 1.18
Question:
Solve
    xDDot + 2*zeta*omegaN*xDot + omegaN**2*x = F0/m*sin(omega*t)
numerically using the RK method.
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
from numerical_solvers import SolveRK14
import collections


# Exact response - answer from Example 1.17
def CartSystemExactResponse(t, m=1.0, omegaN=1.0, zeta=0.03, F0=1.0,
                            omega=0.4):
    x = np.exp(-0.03 * t) * (
        0.03399 * np.cos(0.9995 * t) - 0.4750 * np.sin(0.9995 * t)) + (
            1.190 * np.sin(0.4 * t) - 0.03399 * np.cos(0.4 * t))
    return x


# Equation for the derivatives of the states
def Rates(t, y, m=1.0, omegaN=1.0, zeta=0.03, F0=1.0, omega=0.4):
    f = np.zeros((2, ))
    f[0] = y[1]
    f[1] = ((F0 / m) * np.sin(omega * t) -
            (omegaN**2) * y[0] - 2 * zeta * omegaN * y[1])
    return f


# Plotting functions
def PlotResponse(t, y, tExact=None, xExact=None):
    nStates = y.shape[1]
    _, axs = plt.subplots(nStates)
    units = ["m", "m/s"]
    for idx, ax in enumerate(axs):
        ax.plot(t, y[:, idx], label="RK")
        if (idx == 0) and xExact is not None:
            ax.plot(tExact, xExact, label="Exact")
            ax.legend()
        ax.grid()
        ax.set_ylabel(f"$y_{idx+1}$ ({units[idx]})")
    axs[-1].set_xlabel("Time (s)")
    plt.show()


def PlotFig123(tOut, xOut, sets, tExact, xExact):
    # Note that for some reason the textbook normalises both axes - we replicate 
    # this here for consistency
    _, axs = plt.subplots(5, figsize=(8,12))

    # First plot: exact answer
    axs[0].plot(tExact / tExact[-1], xExact / np.max(xExact), color="black")
    axs[0].set_title("Exact")

    # Other plots: sort by method
    for m, ax in enumerate(axs[1:]):
        rk = m + 1
        colors = ["black", "red"]
        for n, set in enumerate(sets):
            if set.order == rk:
                ax.plot(
                    tOut[n] / tOut[n][-1],
                    xOut[n] / np.max(np.abs(xOut[n])),
                    label=f"h = {set.h}",
                    color=colors[0])
                colors.pop(0)
        ax.set_title(f"RK{rk}")
        ax.legend()
        ax.set_ylim(bottom=-1.,top=1.)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Title
    print("Orbital Mechanics for Engineering Students Example 1.18")

    # (1) Solve individual example
    # Parameters
    y0 = np.array([0, 0])
    tMax = 110.0
    h = 1.0
    order = 4

    # Solve equation numerically
    ys, ts = SolveRK14(Rates, y0, tMax, h, order)

    # Get exact answer
    tExact = np.linspace(0.0, tMax, 5000)
    xExact = CartSystemExactResponse(tExact)

    # Plot results
    PlotResponse(ts, ys, tExact, xExact)

    # (2) Run through different order and h combinations to reproduce Figure 1.23
    TestSet = collections.namedtuple("TestSet", "order h")
    sets = [
        TestSet(1, 0.01), TestSet(1, 0.1), TestSet(2, 0.1), TestSet(2, 0.5),
        TestSet(3, 0.5), TestSet(3, 1.0), TestSet(4, 1.0), TestSet(4, 2.0)
    ]

    xOut = []
    tOut = []
    for set in sets:
        yOut, tOutTmp = SolveRK14(Rates, y0, tMax, set.h, set.order)
        xOut.append(yOut[:, 0])
        tOut.append(tOutTmp)

    PlotFig123(tOut, xOut, sets, tExact, xExact)
