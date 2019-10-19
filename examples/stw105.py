r"""
STW105
======

The STW105 Earth model [Kustowski2008]_ is a one-dimensional model representing average Earth
properties as a function of depth. The model includes the radius, density, seismic velocities,
attenuation (Q), and anisotropic parameter (:math:`\eta`) on the boundaries of several Earth layers.
It's available through IRIS Data Services Products [IRIS2011]_ in a txt file (text).
The data is loaded into :class:`pandas.DataFrame` objects.
"""

import rockhound as rh
import matplotlib.pyplot as plt

# load STW105 into a DataFrame
stw105 = rh.fetch_stw105()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("STW105")
ax = axes[0]
stw105.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [m]")
ax.grid()
ax = axes[1]
for velocity in ["Vpv", "Vsv", "Vph", "Vsh"]:
    stw105.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()

fig, ax = plt.subplots()
stw105.plot("eta", "radius", legend=False, ax=ax)
ax.set_xlabel("eta")
ax.set_ylabel("Radius [m]")
