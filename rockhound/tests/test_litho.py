"""
Test the LiTHO1 model dataset.
"""
import pytest
import numpy.testing as npt

from .. import fetch_litho1
from .. import PROPERTIES, BOUNDARIES


def test_littho():
    """
    Test if loaded files are correct
    """
    dataset = fetch_litho1()
    assert dataset.node.max() == 40962
    assert dataset.node.min() == 1
    assert len(dataset.node.values) == 40962
    assert len(dataset.boundary.values) == 165
    assert tuple(dataset.dims) == ("boundary", "node")
    assert dataset.depth.min() == -5390
    assert dataset.depth.max() == 6371000
    assert dataset.density.min() == 920
    assert dataset.density.max() == 13012.2
    assert dataset.vp.min() == 1500
    assert dataset.vp.max() == 13660.1
    assert dataset.vs.min() == 0
    assert dataset.vs.max() == 7281.7
    assert dataset.qkappa.min() == 0
    assert dataset.qkappa.max() == 0
    assert dataset.qmu.min() == 0
    assert dataset.qmu.max() == 600
    assert dataset.vp2.min() == 1500
    assert dataset.vp2.max() == 13660.1
    assert dataset.vs2.min() == 0
    assert dataset.vs2.max() == 7281.7
    assert dataset.eta.min() == 1
    assert dataset.eta.max() == 1
    assert dataset.title == "LITHO1 moder"
    assert dataset.datum == "WGS84"
    assert dataset.doi == "10.1002/2013JB010626"
    for propertie in PROPERTIES:
        assert dataset[propertie].shape == (40962, 165)


def check_properties():
    """
    Check that all properties values are positive and
    check that one property is nan for a fix node then the others
    properties are nan in this node.
    """


def order_boundaries():
    """
    Check that the correct order of the boundaries depth
    """
