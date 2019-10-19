r"""
ak135-f
=======

The ak135-f Earth model [Kennett1995]_ is a variant of the ak135 Earth model
with the density and Q model from [Montagner1996]_ added.
The ak135-f Earth model is a one-dimensional model representing average Earth properties as a
function of depth. The model includes the depth, density, seismic velocities and attenuation (Q)
on the boundaries of several Earth layers. It's available through IRIS Data Services Products
[IRIS2011]_ in a csv file (comma-separated values). The data is loaded into
:class:`pandas.DataFrame` objects.
"""

import rockhound as rh
import matplotlib.pyplot as plt

# Load ak135f into a DataFrame
ak135f = rh.fetch_ak135f()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("ak135-f")
ax = axes[0]
ak135f.plot("density", "depth", legend=False, ax=ax)
ax.invert_yaxis()
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Depth [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    ak135f.plot(velocity, "depth", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()
