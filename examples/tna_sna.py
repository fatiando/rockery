r"""
TNA/SNA: Tectonic North America/Shield North America
====================================================

The TNA/SNA Earth model [Simmons2010]_ is a one-dimensional model based off of the S velocity models
of [Grand1984]_. This model represents average Earth properties as a function of depth. The model
includes radius and S-wave velocities on the boundaries of several Earth layers. It's available
through IRIS Data Services Products [IRIS2011]_ in a csv file (comma-separated values).
The data is loaded into :class:`pandas.DataFrame` objects.
"""

import rockhound as rh
import matplotlib.pyplot as plt

# load TNA/SNA into a DataFrame
tna_sna = rh.fetch_tna_sna()

# Plot density and velocities
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
fig.suptitle("TNA/SNA")
tna_sna.plot("Vs", "radius", legend=False, ax=ax, label="Vs")
ax.grid()
ax.legend()
ax.set_ylabel("Radius [km]")
ax.set_xlabel("Velocity [km/s]")
plt.show()
