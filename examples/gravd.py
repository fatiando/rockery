"""
GRAV-D
======

GRAV-D (Gravity for the Redefinition of the American Vertical Datum) is
a proposal by the National Geodetic Survey to re-define the vertical datum of
the US by 2022.
"""
import rockhound as rh
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

block = "AS01"
frame = rh.fetch_gravd(block=block)

plt.figure(figsize=(8, 10))
ax = plt.axes(projection=ccrs.Mercator())
tmp = ax.scatter(
    frame.longitude, frame.latitude, c=frame.gravity, s=1, transform=ccrs.PlateCarree(),
)
ax.coastlines(resolution="50m")
ax.set_title("GRAV-D data for block {}".format(block))
gl = ax.gridlines(draw_labels=True, crs=ccrs.PlateCarree())
gl.xlabels_top = False
gl.ylabels_right = False
plt.colorbar(
    tmp,
    ax=ax,
    label="Gravity (mGal)",
    pad=0.03,
    aspect=40,
    shrink=0.95,
    orientation="vertical",
)
plt.tight_layout()
plt.show()
