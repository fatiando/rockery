r"""
PEM-O: Oceanic Parametric Earth Model
=====================================

The PEM-O Earth model [Dziewonsky1975]_ is a one-dimensional model representing average oceanic
Earth properties as a function of radius and depth. The model includes radius, depth, density,
P-wave velocitiy, and S-wave velocity on the boundaries of several Earth layers. It's available
through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values).
The data is loaded into :class:`pandas.DataFrame` objects.
"""

import rockhound as rh
import matplotlib.pyplot as plt

# load PEMO into a DataFrame
pemo = rh.fetch_pemo()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("PEMO")
ax = axes[0]
pemo.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    pemo.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()
