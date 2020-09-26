.. cspell:ignore Nmcps Midx

.. The following fields have to be specified to your card.

Required fields
===============

Names of input root files
-------------------------

One file per line, without tailing characters, such as comma, semicolon and period. Just like in the :code:`TChain::Add` method, absolute, relative paths, and wildcards (:code:`[]?*`) are supported.

Tree name
---------

Name of the :code:`TTree` that contains the MC truth data. Usually, this tree has been written by the :code:`MctruthForTopo` algorithm and is called :code:`"MctruthForTopoAna"`.

Branch name of the number of particles
--------------------------------------

This branch is required for reading the two arrays specified below. In the :code:`MctruthForTopo` package, it is called :code:`"Nmcps"`.

Branch name of the array of particle identifications
----------------------------------------------------

Usually called :code:`"Pid"` in the :code:`MctruthForTopo` package.

Branch name of the array of the mother indices of particles
-----------------------------------------------------------

Usually called :code:`"Midx"` in the :code:`MctruthForTopo` package.

Main name of output files
-------------------------

When you run :code:`topoana.exe` , four files with the same name but in different formats (root/txt/tex/pdf) will be written as output. The filename extensions are appended automatically, so it is not necessary to add these extensions to this field.
