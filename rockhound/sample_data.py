"""
Fetch sample datasets
"""
import pandas as pd
import xarray as xr
from pooch import Decompress

from .registry import REGISTRY


def fetch_baja_bathymetry():
    """
    Fetch sample bathymetry data from Baja California.

    This is the ``@tut_ship.xyz`` sample data from the `GMT
    <http://gmt.soest.hawaii.edu/>`__ tutorial.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The bathymetry data. Columns are longitude, latitude, and bathymetry
        (in meters) for each data point.

    See also
    --------
    setup_baja_bathymetry_map: Utility function to help setup a Cartopy map.

    """
    data_file = REGISTRY.fetch("baja-bathymetry.csv.xz")
    data = pd.read_csv(data_file, compression="xz")
    return data


def fetch_california_gps():
    """
    Fetch sample GPS velocity data from California (the U.S. West coast).

    Velocities and their standard deviations are in meters/year. Height is
    geometric height above WGS84 in meters. Velocities are referenced to the
    North American tectonic plate (NAM08). The average velocities were released
    on 2017-12-27.

    This material is based on EarthScope Plate Boundary Observatory data
    services provided by UNAVCO through the GAGE Facility with support from the
    National Science Foundation (NSF) and National Aeronautics and Space
    Administration (NASA) under NSF Cooperative Agreement No. EAR-1261833.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The GPS velocity data. Columns are longitude, latitude, height
        (geometric, in meters), East velocity (meter/year), North velocity
        (meter/year), upward velocity (meter/year), standard deviation of East
        velocity (meter/year), standard deviation of North velocity
        (meter/year), standard deviation of upward velocity (meter/year).

    See also
    --------
    setup_california_gps_map: Utility function to help setup a Cartopy map.

    """
    data_file = REGISTRY.fetch("california-gps.csv.xz")
    data = pd.read_csv(data_file, compression="xz")
    return data


def fetch_texas_wind():
    """
    Fetch sample wind speed and air temperature data for Texas, USA.

    Data are average wind speed and air temperature for data for February 26
    2018. The original data was downloaded from `Iowa State University
    <https://mesonet.agron.iastate.edu/request/download.phtml>`__.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        Columns are the station ID, longitude, latitude, air temperature in C,
        east component of wind speed in knots, and north component of wind
        speed in knots.

    See also
    --------
    setup_texas_wind_map: Utility function to help setup a Cartopy map.

    """
    data_file = REGISTRY.fetch("texas-wind.csv")
    data = pd.read_csv(data_file)
    return data


def fetch_geoid_earth():
    """
    Fetch a global grid of the geoid height.

    The geoid height is the height of the geoid above (positive) or below
    (negative) the ellipsoid (WGS84). The data are on a regular grid with 0.5
    degree spacing, which was generated from the spherical harmonic model
    EIGEN-6C4 [Forste_etal2014]_ using the `ICGEM Calculation Service
    <http://icgem.gfz-potsdam.de/>`__. See the ``attrs`` attribute of the
    :class:`xarray.Dataset` for information regarding the grid generation.

    Returns
    -------
    grid : :class:`xarray.Dataset`
        The geoid grid (in meters). Coordinates are geodetic latitude and
        longitude.

    """
    fname = REGISTRY.fetch("geoid-earth-0.5deg.nc.xz", processor=Decompress())
    data = xr.open_dataset(fname, engine="scipy").astype("float64")
    return data


def fetch_gravity_earth():
    """
    Fetch a global grid of Earth gravity.

    Gravity is the magnitude of the gravity vector of the Earth (gravitational
    + centrifugal). The gravity observations are at 10 km (geometric) height
    and on a regular grid with 0.5 degree spacing. The grid was generated from
    the spherical harmonic model EIGEN-6C4 [Forste_etal2014]_ using the `ICGEM
    Calculation Service <http://icgem.gfz-potsdam.de/>`__. See the ``attrs``
    attribute of the :class:`xarray.Dataset` for information regarding the grid
    generation.

    If the file isn't already in your data directory, it will be downloaded
    automatically.

    Returns
    -------
    grid : :class:`xarray.Dataset`
        The gravity grid (in mGal). Includes a computation (geometric) height
        grid (``height_over_ell``). Coordinates are geodetic latitude and
        longitude.

    """
    fname = REGISTRY.fetch("gravity-earth-0.5deg.nc.xz", processor=Decompress())
    # The heights are stored as ints and data as float32 to save space on the
    # data file. Cast them to float64 to avoid integer division errors.
    data = xr.open_dataset(fname, engine="scipy").astype("float64")
    return data


def fetch_topography_earth():
    """
    Fetch a global grid of Earth relief (topography and bathymetry).

    The grid is based on the ETOPO1 model [AmanteEakins2009]_. The original
    model has 1 arc-minute grid spacing but here we downsampled to 0.5 degree
    grid spacing to save space and download times. The downsampled grid was
    generated from a spherical harmonic model using the `ICGEM Calculation
    Service <http://icgem.gfz-potsdam.de/>`__. See the ``attrs`` attribute of
    the returned :class:`xarray.Dataset` for information regarding the grid
    generation.

    ETOPO1 heights are referenced to "sea level".

    Returns
    -------
    grid : :class:`xarray.Dataset`
        The topography grid (in meters) relative to sea level. Coordinates are
        geodetic latitude and longitude.

    """
    fname = REGISTRY.fetch("etopo1-0.5deg.nc.xz", processor=Decompress())
    # The data are stored as int16 to save disk space. Cast them to floats to
    # avoid integer division problems when processing.
    data = xr.open_dataset(fname, engine="scipy").astype("float64")
    return data
