"""
Test the Great Britina magnetic anomaly loading function
"""
import numpy.testing as npt

from .. import fetch_britain_magnetic


def test_britain_magnetic():
    "Sanity checks for the loaded dataset"
    data = fetch_britain_magnetic()
    assert data.shape == (541508, 6)
    npt.assert_allclose(data.longitude.min(), -8.65338)
    npt.assert_allclose(data.longitude.max(), 1.92441)
    npt.assert_allclose(data.latitude.min(), 49.81407)
    npt.assert_allclose(data.latitude.max(), 60.97483)
    npt.assert_allclose(data.total_field_anomaly_nt.min(), -3735)
    npt.assert_allclose(data.total_field_anomaly_nt.max(), 2792)
    npt.assert_allclose(data.altitude_m.min(), 201.0)
    npt.assert_allclose(data.altitude_m.max(), 1545.0)
    assert set(data.survey_area.unique()) == {
        "CA55_NORTH",
        "CA55_SOUTH",
        "CA57",
        "CA58",
        "CA59",
        "CA60",
        "CA63",
        "HG56",
        "HG57",
        "HG58",
        "HG61",
        "HG62",
        "HG64",
        "HG65",
    }
