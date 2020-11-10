RockHound
=========

    rock hound : *noun*

    1. A specialist in geology¹
    2. An amateur rock and mineral collector¹
    3. A Python library to download and read common geophysical models and datasets²

    ¹ `Merriam Webster dictionary <https://www.merriam-webster.com/dictionary/rock%20hound>`__ |
    ² Not a real dictionary definition.

`Documentation <https://www.fatiando.org/rockhound>`__ |
`Documentation (dev version) <https://www.fatiando.org/rockhound/dev>`__ |
`Contact <https://gitter.im/fatiando/fatiando>`__ |
Part of the `Fatiando a Terra <https://www.fatiando.org>`__ project

.. image:: https://img.shields.io/pypi/v/rockhound.svg?style=flat-square
    :alt: Latest version on PyPI
    :target: https://pypi.python.org/pypi/rockhound
.. image:: https://img.shields.io/conda/vn/conda-forge/rockhound.svg?style=flat-square
    :alt: Latest version on conda-forge
    :target: https://github.com/conda-forge/rockhound-feedstock
.. image:: https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Ffatiando%2Frockhound%2Fbadge%3Fref%3Dmaster&style=flat-square
    :alt: GitHub Actions status
    :target: https://actions-badge.atrox.dev/fatiando/rockhound/goto?ref=master
.. image:: https://img.shields.io/codecov/c/github/fatiando/rockhound/master.svg?style=flat-square
    :alt: Test coverage status
    :target: https://codecov.io/gh/fatiando/rockhound
.. image:: https://img.shields.io/pypi/pyversions/rockhound.svg?style=flat-square
    :alt: Compatible Python versions.
    :target: https://pypi.python.org/pypi/rockhound
.. image:: https://img.shields.io/badge/doi-10.5281%2Fzenodo.3086001-blue.svg?style=flat-square
    :alt: Digital Object Identifier for the Zenodo archive
    :target: https://doi.org/10.5281/zenodo.3086001

.. placeholder-for-doc-index


Disclaimer
----------

🚨 **This package is in early stages of design and implementation.** 🚨

We welcome any feedback and ideas!
Let us know by submitting
`issues on Github <https://github.com/fatiando/rockhound/issues>`__
or send us a message on our
`Gitter chatroom <https://gitter.im/fatiando/fatiando>`__.


About
-----

RockHound is a Python library to download geophysical models and datasets (PREM,
CRUST1.0, ETOPO1) and load them into Python data structures (pandas, numpy, xarray).

Many of these models use non-conventional file formats or can be tricky
to find on the internet. RockHound knows how to download them if you don't already have
them locally, read the file format, and return a nicely formatted data structure.
Under the hood, it uses `Pooch <https://github.com/fatiando/pooch>`__ to
manage the downloads.


Project goals
-------------

* Download commonly used models and datasets.
* Load data into ``pandas.DataFrame`` (tables) and ``xarray.Dataset`` (grids).
* Only download if needed and check downloads for corruption.
* Provide functions for visualizing complex models and datasets.


Contacting Us
-------------

* Most discussion happens `on Github <https://github.com/fatiando/rockhound>`__.
  Feel free to `open an issue
  <https://github.com/fatiando/rockhound/issues/new>`__ or comment
  on any open issue or pull request.
* We have `chat room on Gitter <https://gitter.im/fatiando/fatiando>`__
  where you can ask questions and leave comments.


Citing RockHound
----------------

This is research software **made by scientists** (see `AUTHORS.md
<https://github.com/fatiando/rockhound/blob/master/AUTHORS.md>`__). Citations help us
justify the effort that goes into building and maintaining this project. If you used
RockHound for your research, please consider citing us.

See our `CITATION.rst file <https://github.com/fatiando/rockhound/blob/master/CITATION.rst>`__
to find out more.


Contributing
------------

Code of conduct
+++++++++++++++

Please note that this project is released with a
`Contributor Code of Conduct <https://github.com/fatiando/rockhound/blob/master/CODE_OF_CONDUCT.md>`__.
By participating in this project you agree to abide by its terms.

Contributing Guidelines
+++++++++++++++++++++++

Please read our
`Contributing Guide <https://github.com/fatiando/rockhound/blob/master/CONTRIBUTING.md>`__
to see how you can help and give feedback.

Imposter syndrome disclaimer
++++++++++++++++++++++++++++

**We want your help.** No, really.

There may be a little voice inside your head that is telling you that you're
not ready to be an open source contributor; that your skills aren't nearly good
enough to contribute.
What could you possibly offer?

We assure you that the little voice in your head is wrong.

**Being a contributor doesn't just mean writing code**.
Equally important contributions include:
writing or proof-reading documentation, suggesting or implementing tests, or
even giving feedback about the project (including giving feedback about the
contribution process).
If you're coming to the project with fresh eyes, you might see the errors and
assumptions that seasoned contributors have glossed over.
If you can write any code at all, you can contribute code to open source.
We are constantly trying out new skills, making mistakes, and learning from
those mistakes.
That's how we all improve and we are happy to help others learn.

*This disclaimer was adapted from the*
`MetPy project <https://github.com/Unidata/MetPy>`__.


License
-------

This is free software: you can redistribute it and/or modify it under the terms
of the **BSD 3-clause License**. A copy of this license is provided in
`LICENSE.txt <https://github.com/fatiando/rockhound/blob/master/LICENSE.txt>`__.


Documentation for other versions
--------------------------------

* `Development <https://www.fatiando.org/rockhound/dev>`__ (reflects the *master* branch on
  Github)
* `Latest release <https://www.fatiando.org/rockhound/latest>`__
* `v0.2.0 <https://www.fatiando.org/rockhound/v0.2.0>`__
* `v0.1.0 <https://www.fatiando.org/rockhound/v0.1.0>`__
