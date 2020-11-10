"""
Load gravity station data from South Africa
"""
import pandas as pd

from .registry import REGISTRY


def fetch_south_africa_gravity():
    """
    Fetch gravity station data from South Africa

    This data base (14559 records), received in January 1986, consists in land
    gravity surveys within the boundaries of the Republic of South Africa. The
    survey was conducted by Dr. R.J. Kleywegt with the contribution of the
    Republic of South Africa, the Department of Mineral and Energy Affairs and
    the Geological Survey. The data was made available by the `National Centers
    for Environmental Information (NCEI) <https://www.ngdc.noaa.gov/>`__
    (formerly NGDC) and are in the `public domain
    <https://www.ngdc.noaa.gov/ngdcinfo/privacy.html#copyright-notice>`__.
    Original data files can be found at:
    https://www.ngdc.noaa.gov/mgg/gravity/1999/data/regional/africa/

    Principal gravity parameters include elevation and observed gravity. The
    observed gravity values are referenced to the International Gravity
    Standardization Net 1971 (IGSN 71). Elevations are referenced above the sea
    level. Both ``longitude`` and ``latitude`` are given in degrees,
    ``elevation`` in meters and ``gravity`` in mGal.

    Returns
    -------
    data : :class:`pandas.DataFrame`
        The gravity data.

    """
    fname = REGISTRY.fetch("south-africa-gravity.ast.xz")
    columns = ["latitude", "longitude", "elevation", "gravity"]
    return pd.read_csv(fname, sep=r"\s+", names=columns, compression="xz")
