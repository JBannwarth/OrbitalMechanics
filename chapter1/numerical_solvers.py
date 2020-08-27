""" Implementation of numerical solvers.
- Runge Kutta (RK) algorithm
- Heun's method
Based on 'Orbital Mechanics for Engineering Students' Section 1.8
Written by: J.X.J. Bannwarth
"""
import numpy as np


def RK14(y, t, f, h, order=4):
    """Use Runge-Kutta algorithm to find y(t+h).

    Parameters
    ----------
    y : numpy.array
        State at time t.
    t : float
        Time y is evaluated at.
    f : function
        Function to compute the derivative of y.
    h : float
        (Fixed) time-step.
    order : int, optional
        Order of the Runge-Kutta algorithm used.

    Returns
    -------
    yN : numpy.array
        Estimated state at time t+h.
    """
    A = {1: [0.0], 2: [0.0, 1.0], 3: [0.0, 0.5, 1.0], 4: [0.0, 0.5, 0.5, 1.0]}
    B = {
        1: None,
        2: [[0.0], [1.0]],
        3: [[0.0, 0.0], [0.5, 0.0], [-1.0, 2.0]],
        4: [[0.0, 0.0, 0.0], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 1.0]],
    }
    C = {
        1: [1.0],
        2: [0.5, 0.5],
        3: [1.0 / 6.0, 2.0 / 3.0, 1.0 / 6],
        4: [1.0 / 6.0, 1.0 / 3.0, 1.0 / 3.0, 1.0 / 6],
    }
    A = np.array(A.get(order, "Invalid order"))
    B = np.array(B.get(order, "Invalid order"))
    C = np.array(C.get(order, "Invalid order"))

    tTilde = t + A * h

    fTilde = np.zeros((order, y.shape[0]))
    yTilde = np.zeros((order, y.shape[0]))

    # Stage 1
    fTilde[0, :] = f(t, y)

    # Stage 2+
    for m in range(1, fTilde.shape[0]):
        yTilde[m, :] = y + h * np.dot(B[m, 0:m], fTilde[0:m, :])
        fTilde[m, :] = f(tTilde[m], yTilde[m, :])

    Phi = np.dot(C, fTilde)
    yN = y + h * Phi
    return yN


def SolveRK14(f, y0, tMax=10.0, h=0.01, order=4):
    """Use Runge-Kutta algorithm numerically solve ODE.

    Parameters
    ----------
    f : function
        Function to compute the derivative of y.
    y0 : numpy.array
        Initial value of state.
    tMax : float
        Time to solve until.
    h : float
        (Fixed) time-step.
    order : int, optional
        Order of the Runge-Kutta algorithm used.

    Returns
    -------
    ys : numpy.array
        State time response.
    ts : numpy.array
        Time vector
    """
    # Assign output vectors
    ts = np.arange(0.0, tMax, h)
    ys = np.zeros((ts.shape[0], y0.shape[0]))

    # Initial conditions if non-zero
    ys[0, :] = y0

    # Solve for each time-step
    for n in range(1, ts.shape[0]):
        ys[n, :] = RK14(ys[n - 1, :], ts[n - 1], f, h, order)

    return (ys, ts)


def SolveHeun(f, y0, tMax=10.0, h=0.01, tol=1.e-6, iterMax=100):
    """Use Heun's method to numerically solve ODE.

    Parameters
    ----------
    f : function
        Function to compute the derivative of y.
    y0 : numpy.array
        Initial value of state.
    tMax : float
        Time to solve until.
    h : float
        (Fixed) time-step.
    tol : float
        Tolerance between y_n+1 and y*.
    iterMax : int
        Maximum number of iterations for a single time-step.

    Returns
    -------
    ys : numpy.array
        State time response.
    ts : numpy.array
        Time vector
    """
    # Assign output vectors
    ts = np.arange(0.0, tMax, h)
    ys = np.zeros((ts.shape[0], y0.shape[0]))

    # Initial conditions if non-zero
    ys[0, :] = y0

    # Solve for each time-step
    for n in range(1, ts.shape[0]):
        d = np.inf
        y1 = ys[n-1, :]

        f1 = f(ts[n-1], y1)
        y2 = y1 + h*f1
        idx = 0
        while d > tol and idx < iterMax:
            y2p = y2
            f2 = f(ts[n], y2p)
            y2 = y1 + h*(f1+f2)/2.

            # Find max error
            d = np.max(np.abs((y2-y2p)/(y2+np.finfo(float).eps)))
            idx += 1
        ys[n, :] = y2p

    return (ys, ts)
