.. cspell:ignore besfs guestpass offlinedb

.. include:: /global.inc

Data sets
=========

This section explains the different data sets that can be processed using BOSS.
There are essentially three types of data files of relevance here:

* **Raw data**

  These are data files containing raw recorded data from either real
  measurements in BESIII or from Monte Carlo simulations. Extension:
  :code:`rtraw` or :code:`raw`, see `here
  <https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/How_to_mix_two_MC_samples>`__
  for how to convert them into each other.

* **Reconstructed data**

  Raw files are too large to be handled in an analysis: the recorded data first
  has to be converted to tracks data. The output of this reconstruction step is
  a DST file. Extension: :code:`dst`.

* **Output from the initial event selection**

  In the analysis step, you analyze the events contained in the DST files. The
  output of that analysis is stored to a :code:`TTree` in a ROOT file.
  Extension: :code:`root`

Locations on the IHEP Server
----------------------------

Inventories of the latest file locations are found on the Offline Software
pages (requires login):


* `Raw data <https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Raw_Data>`_
* `Reconstructed data <https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Production>`_

In general, all data files are located on the BESIII file system
(:code:`besfs`) folders on the :doc:`IHEP Server
</tutorials/getting-started/server>`. There are a few different folders,
because the files have been distributed to different servers.


* :code:`besfs`: contains user files only

* :code:`besfs2`: a symbolic link that points to
  :code:`/besfs3/offline/data/besfs2`. Contains inclusive Monte Carlo samples.

* :code:`besfs3`: file system that contains files of the runs before 2018

* :code:`bes3fs`: a newer file system that contains for instance 2018 data

Within these folders, the data files are located under :code:`offline/data`
(e.g. :code:`/besfs3/offline/data`) and then the BOSS version with which these
files have been created.

.. warning::
  Make sure you do not confuse the numbers when navigating these paths.

Querying for data sets
----------------------

On :code:`lxslc`
^^^^^^^^^^^^^^^^

You can find all information about the data sets through MySQL on
:code:`lxslc`. To open the database, type:

.. code-block:: text

  mysql --user=guest --password=guestpass -h bes3db2.ihep.ac.cn offlinedb

Now it's a matter of searching through the database through MySQL query
commands. Some examples (in this case to find the exact energies of the data
set):


* :code:`show tables;`
* :code:`select * from MeasuredEcms where sample = "4360";` ;
* :code:`select * from MeasuredEcms2 limit 20;`

For a reference of MySQL queries, see `here
<https://dev.mysql.com/doc/refman/8.0/en/>`_.

Note that there are a few BOSS packages that allow you to fetch data from the
MySQL database from the C++ code. The main one is `DatabaseSvc
<http://code.ihep.ac.cn/bes3/BOSS/tree/master/workarea/Database/DatabaseSvc>`_.
For fetching exact beam energy values, use `MeasuredEcmsSvc
<http://code.ihep.ac.cn/bes3/BOSS/tree/master/workarea/Utilities/MeasuredEcmsSvc>`_.

Web interface
^^^^^^^^^^^^^

Alternatively, you can have a look at this page |br|
`http://bes3db.ihep.ac.cn/online/webserver/runinfo/runparams.php
<http://bes3db.ihep.ac.cn/online/webserver/runinfo/runparams.php>`_ |br|
for an overview of run numbers et cetera.


.. toctree::
   :maxdepth: 1

   data/measurements
   data/inclusive
   data/exclusive
