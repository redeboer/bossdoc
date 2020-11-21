# PipiJpsiAlg

See full Doxygen documentation for the `PipiJpsiAlg` on GitPages.

## What does this example package teach?

This example package analyzes
$\psi' \rightarrow \pi\pi J/\psi \rightarrow \pi\pi l l$ (di-lepton) events. In
particular, it will teach you:

- How to access Monte Carlo truth from a DST file using
  [Event::McParticle](http://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html).

- How to store arrays to a `TTree` using
  [NTuple::Array](https://dayabay.bnl.gov/dox/GaudiKernel/html/classNTuple_1_1Array.html)
  and
  [NTuple::addIndexedItem](https://dayabay.bnl.gov/dox/GaudiKernel/html/classNTuple_1_1Tuple.html#a663c6d9a0d9ed46303d836994d3876e8).
  This is useful for storing e.g. an $n$-array of information for $n$ tracks in
  an event. Here, the array is used to store Monte Carlo truth.

- Identifying muons versus electrons using energy of the EMC shower: electrons
  deposit more energy in the EMC.

```{todo}
Still has to be written.

This package introduces several concepts additional to `RhopiAlg`.
```
