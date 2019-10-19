r"""
MEAN
====

The MEAN Earth model is a variant of the IASP91 Earth model. MEAN [Marone2004]_ is a
one-dimensional earth model representing average Earth properties as a function of Earth radius.
This model has parameters for radius, density, P-wave velocity, S-wave velocity, and attenuation
(Q).It's available through IRIS Data Services Products [IRIS2011]_ in a nc file (netCDF). The data
is loaded into :class:`pandas.DataFrame` objects.
"""

import rockhound as rh
import matplotlib.pyplot as plt

# load MEAN into a DataFrame
mean = rh.fetch_mean()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("MEAN")
ax = axes[0]
mean.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    mean.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()
