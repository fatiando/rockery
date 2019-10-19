r"""
PREM: Preliminary Reference Earth Model
=======================================

The Preliminary reference Earth model (PREM) [Dziewonsky1981]_ is a one-dimensional
model representing the average Earth properties as a function of planetary radius.  The
model includes the depth, density, seismic velocities, attenuation (Q) and anisotropic
parameter (:math:`\eta`) on the boundaries of several Earth layers.  The data is loaded
into :class:`pandas.DataFrame` objects, which can be used to plot and make computations.
"""

import rockhound as rh
import matplotlib.pyplot as plt


# Load PREM into a DataFrame
prem = rh.fetch_prem()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("PREM: Preliminary Reference Earth Model")
ax = axes[0]
prem.plot("density", "depth", legend=False, ax=ax)
ax.invert_yaxis()
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Depth [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vpv", "Vph", "Vsv", "Vsh"]:
    prem.plot(velocity, "depth", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()
