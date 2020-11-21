.. include:: /global.inc

RhopiAlg Example Package
========================

What does this example package teach?
-------------------------------------

The :code:`RhopiAlg` is the starting point for beginners using BOSS. It
teaches:

* The usual Gaudi `Algorithm
  <https://dayabay.bnl.gov/dox/GaudiKernel/html/classAlgorithm.html>`_
  structure of the `initialize
  <https://dayabay.bnl.gov/dox/GaudiKernel/html/classAlgorithm.html#ab889608fa1b738d0dbfef7751e8598ae>`_,
  `execute
  <https://dayabay.bnl.gov/dox/GaudiKernel/html/classIAlgorithm.html#a751b04dd35a3877d8799fcd07d0a6892>`_,
  and `finalize
  <https://dayabay.bnl.gov/dox/GaudiKernel/html/classAlgorithm.html#a9ffbd123ceb6c35e7c0344428d911fdc>`_
  steps.

* The use of logging using `MsgStream
  <https://dayabay.bnl.gov/dox/GaudiKernel/html/classMsgStream.html>`_.

* Declaring and booking `NTuple::Tuples
  <https://dayabay.bnl.gov/dox/GaudiKernel/html/classNTuple_1_1Tuple.html>`_
  (the eventual :code:`TTree`) and adding items (the eventual branches) using
  `NTuple::Tuple::addItem
  <https://dayabay.bnl.gov/dox/GaudiKernel/html/classNTuple_1_1Tuple.html#a78033967fbd89f7f18e7d6d7d43f41ac>`_.

* Accessing data of charged tracks and neutral tracks in the using data from
  `EvtRecEvent <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecEvent.html>`_
  and `EvtRecTrack
  <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html>`_ classes.

* Identifying particles (PID) using the `ParticleID
  <http://bes3.to.infn.it/Boss/7.0.2/html/classParticleID.html>`_ class.

* Making a selection of these tracks (using iterators) over which you loop
  again later.

* Applying a Kalman kinematic fit with `constraints
  <http://bes3.to.infn.it/Boss/7.0.2/html/classTrackPool.html#5ecaf22a24d60b2979d0ccd3b0c1df10>`_
  and a `resonance
  <http://bes3.to.infn.it/Boss/7.0.2/html/classKalmanKinematicFit.html#1163bb8ab7e0ebc53c81b2a4d840ebb0>`_
  using `KalmanKinematicFit
  <http://bes3.to.infn.it/Boss/7.0.2/html/classKalmanKinematicFit.html>`_.

* Computing invariant masses using `HepLorentzVector
  <https://www-zeuthen.desy.de/geant4/clhep-2.0.4.3/classCLHEP_1_1HepLorentzVector.html>`_
  from the CLHEP library.

* Computing the angle between a photon and a pion.

* Reconstructed data from the detectors is accessed through the classes in the
  below table. This package only makes use of the MDC, EMC, and TOF detectors.

.. list-table::
  :header-rows: 1

  * - Detector
    -
    - Class
    - Accessed through
  * - **MDC**
    - **Main Drift Chamber**
    - `RecMdcTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classRecMdcTrack.html>`_
    - `EvtRecTrack::mdcTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html#b20b980cd2f97e76870d85310f3701a9>`_
  * - **MDC**
    - :math:`dE/dx` **info**
    - `RecMdcDedx <http://bes3.to.infn.it/Boss/7.0.2/html/classRecMdcDedx.html>`_
    - `EvtRecTrack::mdcDedx <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html#946473c9e8d949a44e1254f70014ce6e>`_
  * - **MDC**
    - **Kalman track**
    - `RecMdcKalTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classRecMdcKalTrack.html>`_
    - `EvtRecTrack::mdcKalTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html#b992dd00fcd938cf17b4a6090ca16a81>`_
  * - **TOF**
    - **Time-of-Flight**
    - `RecTofTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classRecTofTrack.html>`_
    - `EvtRecTrack::tofTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html#2c997882dd8ad532f01f0a10f93de2a0>`_
  * - **EMC**
    - **EM-Calorimeter**
    - `RecEmcShower <http://bes3.to.infn.it/Boss/7.0.2/html/classRecEmcShower.html>`_
    - `EvtRecTrack::emcShower <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html#ac7a7d3cc71a349c2e9de6cf19865ecf>`_
  * - MUC
    - Muon Chamber
    - `RecMucTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classRecMucTrack.html>`_
    - `EvtRecTrack::mucTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html#a3a8ae89c68adcec20ac3fb7248a1b31>`_
  * - <>
    - *Extension through all*
    - `RecExtTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classRecExtTrack.html>`_
    - `EvtRecTrack::extTrack <http://bes3.to.infn.it/Boss/7.0.2/html/classEvtRecTrack.html#3fd94beab03bbde9f056f832b106868a>`_


Introduction
------------

One of the basic physics analysis packages that is already provided in BOSS is
the :code:`RhopiAlg` package. Within BESIII, almost everyone knows it, because
it is used as the starting point for developing your own initial event
selection packages. :code:`RhopiAlg` is an illustration of a typical procedure
in particle physics: reconstructing a decayed particle. For this, you will have
to make apply cuts on measured parameters and this package is an illustration
of this procedure.

The :code:`RhopiAlg` analyzes the decay of the :math:`\rho(770)` meson. As you
can see in the in the `PDG listing for this meson
<http://pdg.lbl.gov/2018/listings/rpp2018-list-rho-770.pdf>`_, the
:math:`\rho(770)` meson predominantly decays through
:math:`\rho\rightarrow\pi\pi` (almost :math:`100\%`), whether it concerns a
:math:`\rho^+` , :math:`\rho^0` , or :math:`\rho^-`. This means that we can
reconstruct this meson purely through this *2-particle decay mode*.

Additionally, when we consider the charged :math:`\rho^\pm` mesons, one of the
decay products is the neutral pion: :math:`\rho^\pm \rightarrow \pi^\pm\pi^0`.
This meson is again neutral and cannot be detected, so has to be reconstructed.
But here again, there is one dominant decay mode: :math:`\pi^0 \rightarrow
\gamma\gamma` (:math:`98.823 \pm 0.034 \%`, see `its PDG listing
<http://pdg.lbl.gov/2018/listings/rpp2018-list-pi-zero.pdf>`_). This means that
we can reconstruct the :math:`\rho^\pm` meson almost exclusively through its
:math:`\rho^\pm \rightarrow \pi^\pm\pi^0 \rightarrow \pi^\pm\gamma\gamma` decay
channel.

In reconstructing :math:`\pi^0` and :math:`\rho^0`, you will run into another
common phenomenon in hadron research: the width of the decaying particle. The
width of :math:`\rho^0` is much wider than :math:`\pi^0` and therefore results
in interesting differences in the eventual invariant mass spectra. In the final
event selection, you will for instance see that a fit of the invariant mass
peaks results in different widths.

Where to find it?
-----------------

The original :code:`RhopiAlg` package (version :code:`0.0.23`) is located here,

.. code-block:: text

  /afs/ihep.ac.cn/bes3/offline/Boss/$BOSSVERSION/Analysis/Physics/RhopiAlg/RhopiAlg-00-00-23

You can also `find the RhopiAlg package in the BOSS Tutorials repository
<http://code.ihep.ac.cn/bes3/BOSS_Tutorials/-/tree/master/RhopiAlg/RhopiAlg-00-00-23>`_.

How to compile and run?
-----------------------

See :ref:`summary of Set up a BOSS package
<tutorials/getting-started/setup-package:Summary>` and :doc:`Running jobs
</tutorials/getting-started/jobs>`. An `example of a analysis job option file
for RhopiAlg
<https://github.com/redeboer/BOSS_IniSelect_ORIGINAL/blob/b48291704f1b1df6a9953fd50689b9039f064815/workarea/TestRelease/TestRelease-00-00-00/run/jobOptions_ana_rhopi.txt>`_
is found under :code:`run` :ref:`in the TestRelease package
<tutorials/getting-started/setup-package:The TestRelease package>`.

The parameter :code:`EventCnvSvc.digiRootInputFile` lists the input files. This
is currently :code:`rhopi.dst` (namely the output after running the
:code:`jobOptions_rec.txt` job), but you can also feed it other DST files, such
as :ref:`the ones reconstructed from BESIII data or inclusive Monte Carlo
samples <tutorials/getting-started/server:Important data paths>`.

Description of source code
--------------------------

.. warning::
  The sections below are incomplete and it is not yet decided whether it is
  useful to describe the source code in words.

Declaring and defining properties like cuts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :code:`header :code:`.h` file
<https://github.com/redeboer/BOSS_IniSelect_ORIGINAL/blob/b48291704f1b1df6a9953fd50689b9039f064815/workarea/Analysis/Physics/RhopiAlg/RhopiAlg-01-00-00/RhopiAlg/RhopiAlg.h#L42>`_
for declarations and :code:`source `.cxx` code
<https://github.com/redeboer/BOSS_IniSelect_ORIGINAL/blob/master/workarea/Analysis/Physics/RhopiAlg/RhopiAlg-01-00-00/src/RhopiAlg.cxx>`_
for definitions of cuts.

Determining vertex position
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writing properties
^^^^^^^^^^^^^^^^^^

Looping over charged and neutral tracks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kalman kinematic :math:`n`-constraints fit procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :code:`fit4c` refers to the 4-constraints coming from the original
  :math:`\pi^0 \rightarrow \gamma\gamma` meson (or other mesons, depending on
  the collision energy), namely, the 4-momentum of the system (collision energy
  and sum of the 3-momenta). Note that the :math:`\chi^2_\text{red}` of the fit
  is the same for any combination, as the for constraints are the same in each
  event.

* :code:`fit5c`  is used when an additional constraint is applied. In the
  :code:`RhopiAlg` package, this fifth constraint refers to the constraint
  reconstruction of :math:`\rho^\pm \rightarrow \pi^\pm\pi^0 \rightarrow
  \pi^\pm\gamma\gamma`, namely the mass of the pion.

Cut flow
^^^^^^^^

Output :code:`root` file
------------------------

.. warning::
  General description of how to read the output ROOT file.
