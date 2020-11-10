"""
Load the GRAV-D Airborne Gravity data for United States
"""
import os
import numpy as np
import pandas as pd
from pooch import Unzip

from .registry import REGISTRY


ZONES = {
    "Alaska North": [
        "AN01",
        "AN02",
        "AN03",
        "AN04",
        "AN05",
        "AN06",
        "AN07",
        "AN08",
        "AN09",
    ],
    "Alaska South": [
        "AS01",
        "AS02",
        "AS03",
        "AS04",
        "AS05",
        "AS06",
        "AS07",
        "AS08",
        "AS09",
    ],
    "Atlantic South": ["TS01"],
    "Central North": ["CN01", "CN02", "CN03", "CN04", "CN05"],
    "Central South": [
        "CS01",
        "CS02",
        "CS03",
        "CS04",
        "CS05",
        "CS06",
        "CS07",
        "CS08",
        "CS09",
    ],
    "Eastern North": [
        "EN01",
        "EN02",
        "EN03",
        "EN04",
        "EN05",
        "EN06",
        "EN07",
        "EN08",
        "EN09",
        "EN10",
    ],
    "Eastern South": ["ES01", "ES02", "ES03", "ES04", "ES05", "ES06", "ES07"],
    "Mountain South": ["MS01", "MS02", "MS03", "MS04", "MS05"],
    "Pacific North": ["PN01", "PN02", "PN03"],
    "Pacific South": ["PS01", "PS02"],
}
BLOCKS = [zone[i] for zone in ZONES.values() for i in range(len(zone))]
COLUMNS_NAMES = [
    "flight_id",
    "id_or_date",
    "latitude",
    "longitude",
    "height",
    "gravity",
]


def fetch_gravd(zone=None, block=None, *, load=True):
    """
    Fetch GRAV-D Airborne Gravity data for United States

    Parameters
    ----------
    zone : str or None
        Desired survey zone. Either `zone` or `block` must be passed.
        Availabe zones are:
          - ``"Alaska North" ``
          - ``"Alaska South"``
          - ``"Atlantic South"``
          - ``"Central North"``
          - ``"Central South"``
          - ``"Eastern North"``
          - ``"Eastern South"``
          - ``"Mountain South"``
          - ``"Pacific North"``
          - ``"Pacific South"``
    block : str or None
        Desired survey block. Either `zone` or `block` must be passed.
    """
    if zone is not None and block is not None:
        raise ValueError("Both zone and block provided. Only one is allowed.")
    if zone is None and block is None:
        raise ValueError("Either a zone or a block must be provided.")
    if zone is not None:
        if zone not in ZONES:
            raise ValueError(
                "Passed zone '{}' is not a valid GRAV-D zone.".format(zone)
            )
        blocks = tuple(b for b in ZONES[zone])
    if block is not None:
        if block not in BLOCKS:
            raise ValueError(
                "Passed block '{}' is not a valid GRAV-D block.".format(block)
            )
        blocks = (block,)
    fnames = list(
        fname
        for b in blocks
        for fname in REGISTRY.fetch(
            "NGS_GRAVD_Block_{}_BETA1.zip".format(b), processor=Unzip()
        )
    )
    if not load:
        return fnames
    frames = [_load_block_file(b, fnames) for b in blocks]
    if len(frames) > 1:
        frame = pd.concat(frames, ignore_index=True)
    else:
        frame = frames[0]
    return frame


def _load_block_file(block, fnames):
    """
    Load block file into a pandas.Dataframe
    """
    fname_first_part = "NGS_GRAVD_Block_{}_Gravity_Data".format(block)
    (fname,) = tuple(
        f
        for f in fnames
        if os.path.basename(f).startswith(fname_first_part)
        and f.endswith(".txt")
        and "supplementary" not in os.path.basename(f)
    )
    return pd.read_csv(fname, sep=r"\s+", names=COLUMNS_NAMES, usecols=np.arange(6))
