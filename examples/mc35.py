r"""
MC35
====

The MC35 Earth model [VanderLee1997]_ is a one-dimensional model based off of the PEM-C. This model
represents average Earth properties as a function of depth. The model includes the depth and S-wave
velocities on the boundaries of several Earth layers. It's available through IRIS Data Services
Products [IRIS2011]_ in a csv file (comma-separated values). The data is loaded into
:class:`pandas.DataFrame` objects.
"""

import rockhound as rh
import matplotlib.pyplot as plt

# load MC35 into a DataFrame
mc35 = rh.fetch_mc35()

# Plot density and velocities
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
fig.suptitle("MC35")
mc35.plot("Vs", "depth", legend=False, ax=ax, label="Vs")
ax.invert_yaxis()
ax.grid()
ax.legend()
ax.set_ylabel("Depth [km]")
ax.set_xlabel("Velocity [km/s]")
plt.show()
