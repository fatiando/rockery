"""
Test the South Africa gravity loading function
"""
import numpy.testing as npt

from .. import fetch_south_africa_gravity


def test_south_africa_gravity():
    "Sanity checks for the loaded dataset"
    data = fetch_south_africa_gravity()
    assert data.shape == (14559, 4)
    npt.assert_allclose(data.longitude.min(), 11.90833)
    npt.assert_allclose(data.longitude.max(), 32.74667)
    npt.assert_allclose(data.latitude.min(), -34.996)
    npt.assert_allclose(data.latitude.max(), -17.33333)
    npt.assert_allclose(data.elevation.min(), -1038.00)
    npt.assert_allclose(data.elevation.max(), 2622.17)
    npt.assert_allclose(data.gravity.min(), 978131.3)
    npt.assert_allclose(data.gravity.max(), 979766.65)
