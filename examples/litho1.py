"""
LITHO1.0 - An updated crust and lithospheric model of the Earth
===============================================================
The LITHO1.0 model is a 1° tessellated model of the crust and uppermost
mantle of the earth, extending into the upper mantle to include the
lithospheric lid and underlying asthenosphere.
More information at the
`model <https://igppweb.ucsd.edu/~gabi/litho1.0.html>`__
website.
"""

import rockhound as rh
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cmocean

# Fetch all LiTHO model
litho = rh.fetch_litho1()
print(litho)

# Extract the information about the Moho boundary.
# It is ralated with the CRUST3-BOTTOM boundary in the LITHO1 model.
moho = litho.sel(boundary="CRUST3-BOTTOM")

# Plot the Moho depth
plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Robinson())
pc = plt.scatter(
    moho.longitude,
    moho.latitude,
    c=moho.depth.values,
    s=0.5,
    transform=ccrs.PlateCarree(),
    cmap=cmocean.cm.thermal_r,
)
plt.colorbar(
    pc,
    ax=ax,
    label="Depth (m)",
    pad=0.05,
    aspect=40,
    shrink=0.7,
    orientation="horizontal",
)
ax.set_title("LITHO1 Model: Moho depth")
ax.set_global()
ax.coastlines()
plt.show()
