"""
Test the PREM loading function.
"""
from ..mcmurray_facies import fetch_mcmurray_facies


def test_mcmurray_facies_columns():
    """Sanity checks for the mcmurray_facies DataFrame"""
    mcmurray_facies = fetch_mcmurray_facies(abbreviations_only=True, load=True)
    columns = str(
        [
            "Unnamed: 0",
            "CALI",
            "COND",
            "DELT",
            "DEPT",
            "DPHI",
            "DT",
            "GR",
            "ILD",
            "ILM",
            "NPHI",
            "PHID",
            "RHOB",
            "SFL",
            "SFLU",
            "SN",
            "SP",
            "UWI",
            "SitID",
            "lat",
            "lng",
            "Depth",
            "LithID",
            "W_Tar",
            "SW",
            "VSH",
            "PHI",
            "RW",
            "lithName",
        ]
    )
    mcmurray_facies_columns = str(list(mcmurray_facies.columns))
    assert mcmurray_facies_columns == columns


def test_mcmurray_facies_length():
    """Sanity checks for the mcmurray_facies DataFrame"""
    mcmurray_facies = fetch_mcmurray_facies(abbreviations_only=True, load=True)
    assert len(mcmurray_facies) == 328204
