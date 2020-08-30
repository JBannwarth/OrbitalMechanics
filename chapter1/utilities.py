""" Utility scripts
Written by: J.X.J. Bannwarth
"""

def PrintVec(v, name, unit = '', big=False):
    if big:
        print(f"{name} = {v[0]:.4f} I + {v[1]:.4f} J + {v[2]:.4f} K {unit}")
    else:
        print(f"{name} = {v[0]:.4f} i + {v[1]:.4f} j + {v[2]:.4f} k {unit}")
