""" Orbital Mechanics for Engineering Students Example 2.3
Question:
    A 1000 kg satellite orbits earth. Given the initial conditions
        R_0 = 8000*i + 6000*k
        V_0 = 7*j km/s
    Solve the relative motion of the satellite with respect to the earth from
    t = 0 to t = 4 hours.
    Also determine the minimum and maximum distance from the earth.
Written by: J.X.J. Bannwarth
"""
import numpy as np
from orbitutils.orbiting_bodies import orbit
import plotly.graph_objects as go

# Title
print("Orbital Mechanics for Engineering Students Example 2.3")

# Constants
r_E = 6378.
R_0 = np.array([8000., 0., 6000.])  # km
V_0 = np.array([0., 7., 0.])  # km/s
M = np.array([1000., 5.974e24])  # kg
t_span = np.array([0., 4. * 60. * 60.])  # s

# Solve the problem
Y, t = orbit(R_0, V_0, M, t_span)
R = Y[:, 0:3]
V = Y[:, 3:6]

# Find the largest distance
r = np.linalg.norm(R, axis=1) - r_E
v = np.linalg.norm(V, axis=1)
max_idx = np.argmax(r)
min_idx = np.argmin(r)

# Print the results
print(
    f"The minimum altitude is {r[min_idx]:.0f} km at t = {t[min_idx]:.0f} s," +
    " and the speed at that point is {v[min_idx]:.2f} km/s")
print(
    f"The maximum altitude is {r[max_idx]:.0f} km at t = {t[max_idx]:.0f} s," +
    " and the speed at that point is {v[max_idx]:.2f} km/s")

# Plot the results
azimuth, elevation = np.mgrid[0:2 * np.pi:100j, -np.pi:np.pi:100j]
x_E = r_E * np.cos(azimuth) * np.sin(elevation)
y_E = r_E * np.sin(azimuth) * np.sin(elevation)
z_E = r_E * np.cos(elevation)

# Make the equator slightly bigger to be visible clearly
x_equator = r_E * np.cos(np.linspace(0, 2 * np.pi, 100)) * 1.002
y_equator = r_E * np.sin(np.linspace(0, 2 * np.pi, 100)) * 1.002
z_equator = np.zeros(x_equator.shape)

fig = go.Figure(data=[
    go.Surface(x=x_E, y=y_E, z=z_E, colorscale=[[0, "gray"], [1, "gray"]],
               showscale=False),
    go.Scatter3d(x=x_equator, y=y_equator, z=z_equator,
                 mode="lines", line=dict(color="blue"), name="Equator"),
    go.Scatter3d(x=R[:, 0], y=R[:, 1], z=R[:, 2], mode="lines",
                 line=dict(color="black"), name="Path"),
    go.Scatter3d(x=R[(0, -1), (0, 0)], y=R[(0, -1), (1, 1)], z=R[(0, -1), (2, 2)],
                 mode="markers", marker=dict(color="black"), name="End points")
])

fig.update_layout(
    xaxis=dict(title_text="x (km)"),
    yaxis=dict(title_text="y (km)"),
)

fig.update_layout(
    scene=dict(
        dragmode="turntable",
        xaxis=dict(
            title_text="x (km)",
            showgrid=False,
        ),
        yaxis=dict(
            title_text="y (km)",
            showgrid=False,
        ),
        zaxis=dict(
            title_text="z (km)",
            showgrid=False,
        ),
        annotations=[dict(
            showarrow=False,
            x=R[0, 0],
            y=R[0, 1],
            z=R[0, 2],
            text="$t_0$",
            xanchor="left",
            xshift=10,
        ), dict(
            showarrow=False,
            x=R[-1, 0],
            y=R[-1, 1],
            z=R[-1, 2],
            text="$t_f$",
            xanchor="left",
            xshift=10,
        )
        ]
    )
)


fig.show()
