"""
Wind speed data from Texas
==========================

This is average wind speed and air temperature for data for the state of Texas,
USA, on February 26 2018. The original data was downloaded from `Iowa State
University <https://mesonet.agron.iastate.edu/request/download.phtml>`__.
"""
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import rockhound as rh


# The data are in a pandas.DataFrame
data = rh.fetch_texas_wind()
print(data.head())

# Make a Mercator map of the data using Cartopy
plt.figure(figsize=(8, 6))
ax = plt.axes(projection=ccrs.Mercator())
ax.set_title("Wind speed and air temperature for Texas")
# Plot the air temperature as colored circles and the wind speed as vectors.
plt.scatter(
    data.longitude,
    data.latitude,
    c=data.air_temperature_c,
    s=100,
    cmap="plasma",
    transform=ccrs.PlateCarree(),
)
plt.colorbar().set_label("Air temperature (C)")
ax.quiver(
    data.longitude.values,
    data.latitude.values,
    data.wind_speed_east_knots.values,
    data.wind_speed_north_knots.values,
    width=0.003,
    transform=ccrs.PlateCarree(),
)

# Add tick labels and land and ocean features to the map.
region = (-107, -93, 25.5, 37)
crs = ccrs.PlateCarree()
ax.add_feature(cfeature.LAND, facecolor="#dddddd")
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.STATES, linewidth=0.1)
ax.set_extent(region, crs=crs)
ax.set_xticks(np.arange(-106, -92, 3), crs=crs)
ax.set_yticks(np.arange(27, 38, 3), crs=crs)
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

plt.tight_layout()
plt.show()
