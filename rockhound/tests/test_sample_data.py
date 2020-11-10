"""
Test sample data loading functions
"""
import numpy.testing as npt

from .. import (
    fetch_geoid_earth,
    fetch_gravity_earth,
    fetch_topography_earth,
    fetch_texas_wind,
    fetch_baja_bathymetry,
    fetch_california_gps,
)


def test_geoid_earth():
    "Sanity checks for the loaded grid"
    grid = fetch_geoid_earth()
    assert grid.geoid.shape == (361, 721)
    npt.assert_allclose(grid.geoid.min(), -106.257344)
    npt.assert_allclose(grid.geoid.max(), 84.722744)


def test_gravity_earth():
    "Sanity checks for the loaded grid"
    grid = fetch_gravity_earth()
    assert grid.gravity.shape == (361, 721)
    npt.assert_allclose(grid.gravity.max(), 9.8018358e05)
    npt.assert_allclose(grid.gravity.min(), 9.7476403e05)
    assert grid.height_over_ell.shape == (361, 721)
    npt.assert_allclose(grid.height_over_ell, 10000)


def test_topography_earth():
    "Sanity checks for the loaded grid"
    grid = fetch_topography_earth()
    assert grid.topography.shape == (361, 721)
    npt.assert_allclose(grid.topography.max(), 5651, atol=1)
    npt.assert_allclose(grid.topography.min(), -8409, atol=1)


def test_fetch_texas_wind():
    "Make sure the data are loaded properly"
    data = fetch_texas_wind()
    assert data.size == 1116
    assert data.shape == (186, 6)
    assert all(
        data.columns
        == [
            "station_id",
            "longitude",
            "latitude",
            "air_temperature_c",
            "wind_speed_east_knots",
            "wind_speed_north_knots",
        ]
    )


def test_fetch_baja_bathymetry():
    "Make sure the data are loaded properly"
    data = fetch_baja_bathymetry()
    assert data.size == 248910
    assert data.shape == (82970, 3)
    assert all(data.columns == ["longitude", "latitude", "bathymetry_m"])


def test_fetch_california_gps():
    "Make sure the data are loaded properly"
    data = fetch_california_gps()
    assert data.size == 22122
    assert data.shape == (2458, 9)
    columns = [
        "latitude",
        "longitude",
        "height",
        "velocity_north",
        "velocity_east",
        "velocity_up",
        "std_north",
        "std_east",
        "std_up",
    ]
    assert all(data.columns == columns)
