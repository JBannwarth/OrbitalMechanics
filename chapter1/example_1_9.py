""" Orbital Mechanics for Engineering Students Example 1.9
Question:
The *Atlantis* orbiter weighs 239,255 lb prior to liftoff. On orbit 18 at an altitude of 350 km, the orbiter is 236,900 lb.
(a) What is the mass (kg) of Atlantis on the launchpad and in orbit?
(b) If no mass is lost between launch and orbin 18, what is the weight of *Atlantis* in pounds?
Written by: J.X.J. Bannwarth
"""

g0 = 9.807 # m/s^2
lb2kg = 0.4536 # kg

wLiftoff = 239255.  # lb
wOrbit18 = 236900. # lb

rE = 6378000. # km
zOrbit18 = 350000. # km

# (a)
mLiftoff = wLiftoff*lb2kg
mOrbit18 = wOrbit18*lb2kg
print(f"m_launchpad = {mLiftoff:.2f} kg, m_orbit18 = {mOrbit18:.2f} kg")

# (b)
g = g0 / (1. + zOrbit18/rE)**2
wOrbit18NoLoss = wLiftoff*g/g0
print(f"w_orbit18 = {wOrbit18NoLoss:.2f} lbf")
