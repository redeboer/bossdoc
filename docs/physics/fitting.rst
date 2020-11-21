
Fitting procedures
==================

Fitting meson resonances
------------------------

Best overview of types of fits and theoretical motivations for each of those
can be found in section `"Resonances" of the *PDG*
<http://pdg.lbl.gov/2018/reviews/rpp2018-rev-resonances.pdf>`_.

* BESIII is a *formation experiment*.

See documentation for all :code:`RooFit` parametrizations `here
<https://root.cern/doc/master/group__Roofit.html>`__.

Single and double Gaussian
^^^^^^^^^^^^^^^^^^^^^^^^^^

Characterization of detector resolution(s).

Breit-Wigner parametrization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Only works in case of *narrow structure* and if there are no other resonances
  nearby

* Can be used to extract *pole parameters* such as particle width

* Possible: energy dependent parameters

* Convolution of a Breit-Wigner with a Gaussian is called a *Voigtian* (see
  `RooVoigtian <https://root.cern.ch/doc/master/classRooVoigtian.html>`_).

Flatté parametrization
^^^^^^^^^^^^^^^^^^^^^^

* Analytical continuation of the Breit-Wigner parametrization
* Does not allow for extraction of pole parameters, only ratios


Background shapes
-----------------

* `Polynomial <https://root.cern/doc/master/classRooPolynomial.html>`_ ​

* ​ `Chebychev polynomial <https://root.cern.ch/doc/master/classRooChebychev.html>`_ ​

* ​ `Argus background shape <https://root.cern/doc/master/classRooArgusBG.html>`_ ​


Other literature
----------------

* `LHCb GitBook on RooFit
  <https://lhcb.github.io/ostap-tutorials/fitting/decorations.html>`_

* `Example scripts for RooFit
  <https://root.cern.ch/root/html/tutorials/roofit/index.html>`_ (see overview
  of descriptions `here
  <https://root.cern.ch/doc/master/group__tutorial__roofit.html>`__)
