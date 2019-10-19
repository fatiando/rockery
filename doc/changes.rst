.. _changes:

Changelog
=========

Version 0.1.0
-------------

*Released on: 2019/05/21*

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3086002.svg
   :target: https://doi.org/10.5281/zenodo.3086002

First release of Rockhound. Easily download geophysical models and datasets (PREM,
CRUST1.0, ETOPO1 and more) and load them into Python data structures (pandas, numpy,
xarray).

Available models and datasets:

- ETOPO1 [AmanteEakins2009]_
- PREM [Dziewonsky1981]_
- Bedmap2 [BEDMAP2]_
- Age of the oceanic lithosphere [Muller2008]_

Features:

- Use `Pooch <https://www.fatiando.org/pooch>`__ to download remote files, check if they
  are not corrupted and decompress files if necessary.
