r"""
PEM-A: Average Parametric Earth Model
=====================================

The PEM-A Earth model [Dziewonsky1975]_ is a weighted average of both the
PEM-O Earth model and the PEM-C Earth model. It is a one-dimensional model
representing average Earth properties as a function of depth. The model
includes the radius, depth, density, P-wave velocity, and S-wave velocity on the boundaries of
several Earth layers. It's available through IRIS Data Services Products [IRIS2011]_
in a csv file (comma-separated values). The data is loaded into
:class:`pandas.DataFrame` objects.
"""
import rockhound as rh
import matplotlib.pyplot as plt

# load PEMA into a DataFrame
pema = rh.fetch_pema()

# Plot density and velocities
fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
fig.suptitle("PEMA")
ax = axes[0]
pema.plot("density", "radius", legend=False, ax=ax)
ax.set_xlabel("Density [g/cm³]")
ax.set_ylabel("Radius [km]")
ax.grid()
ax = axes[1]
for velocity in ["Vp", "Vs"]:
    pema.plot(velocity, "radius", legend=False, ax=ax, label=velocity)
ax.grid()
ax.legend()
ax.set_xlabel("Velocity [km/s]")
plt.show()
