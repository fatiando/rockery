"""
Load the Bedmap2 datasets for Antarctica.
"""
import os
import tempfile
from zipfile import ZipFile

import xarray as xr

from .registry import REGISTRY

DATASETS = [
    "bed",
    "surface",
    "thickness",
    "icemask_grounded_and_shelves",
    "rockmask",
    "lakemask_vostok",
    "bed_uncertainty",
    "thickness_uncertainty_5km",
    "data_coverage",
    "geoid",
]


def fetch_bedmap2(datasets=DATASETS, load=True):
    """
    Download and load Bedmap2 model datasets.

    It downloads the Bedmap2 model in `tiff` format, checks its integrity
    through `pooch` and creates a :class:`xarray.DataArray` with the data from
    the wanted file.

    References:
    [BEDMAP2]_

    Parameters
    ----------
    datasets : list
        Datasets that wants to be loaded from the Bedmap2 model.
        The available datasets are: `bed`, `surface`, `thickness`,
        `icemask_grounded_and_shelves`, `rockmask`, `lakemask_vostok`,
        `bed_uncertainty`, `thickness_uncertainty_5km`, `data_coverage` and
        `geoid`. For more information read the `bedmap2_readme.txt` file.
    load : bool
        Wether to load the data into an :class:`xarray.Dataset` or just return the
        path to the downloaded data.

    Returns
    -------
    da : :class:`xarray.DataArray`
        Data array containing the loaded Bedmap2 file.
    """
    for dataset in datasets:
        if dataset not in DATASETS:
            raise IOError("Dataset {} not found in bedmap2_tiff.zip".format(dataset))
    available_datasets = dict(
        zip(DATASETS, ["bedmap2_{}.tif".format(dataset) for dataset in DATASETS])
    )
    available_datasets["geoid"] = "gl04c_geiod_to_WGS84.tif"
    fname = REGISTRY.fetch("bedmap2_tiff.zip")
    if not load:
        return fname

    arrays = []
    for dataset in datasets:
        with tempfile.TemporaryDirectory() as tempdir:
            # Decompress the file into a temporary file so we can load it with xr
            # The .tif files inside the zip are located inside a bedmap2_tiff directory
            with ZipFile(fname, 'r') as zip_file:
                zip_file.extract(
                    os.path.join("bedmap2_tiff", available_datasets[dataset]),
                    path=tempdir
                )
            arrays.append(
                xr.open_rasterio(
                    os.path.join(tempdir, "bedmap2_tiff", available_datasets[dataset])
                )
            )
    ds = xr.concat(arrays)
    return ds
