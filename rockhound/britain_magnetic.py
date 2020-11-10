"""
Load total-field magnetic field anomaly dataset of Great Britain
"""
import pandas as pd

from .registry import REGISTRY


def fetch_britain_magnetic():
    """
    Fetch total-field magnetic anomaly data of Great Britain.

    These data are a complete airborne survey of the entire Great Britain
    conducted between 1955 and 1965. The data are made available by the
    British Geological Survey (BGS) through their `geophysical data portal
    <https://www.bgs.ac.uk/products/geophysics/aeromagneticRegional.html>`__.

    License: `Open Government License
    <http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/>`__

    The columns of the data table are longitude, latitude, total-field magnetic
    anomaly (nanoTesla), observation height relative to the WGS84 datum (in
    meters), survey area, and line number and line segment for each data point.

    Latitude, longitude, and elevation data converted from original OSGB36
    (epsg:27700) coordinate system to WGS84 (epsg:4326) using to_crs function
    in GeoPandas.

    See the original data for more processing information.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The magnetic anomaly data.

    """
    return pd.read_csv(REGISTRY.fetch("britain-magnetic.csv.xz"), compression="xz")
