.. cspell:ignore TESTRELEASEROOT

Running jobs
============

.. todo::
  Write section about `job submission through macros
  <http://afsapply.ihep.ac.cn/cchelp/en/local-cluster/jobs/HTCondor/#3213-tips-of-using-hepjob>`_.

Particle physicists perform analyzes on either data from measurements or on
data from Monte Carlo simulation. In BOSS, it is possible to generate your own
Monte Carlo simulations and to treat its output as ordinary data. There are
there for three basic steps in running a Monte Carlo job on BOSS:

#. :code:`sim`: you perform a Monte Carlo simulation and generate a raw data
   file (:code:`rtraw`).

#. :code:`rec`: you reconstruct particle tracks from the raw data and write out
   a reconstructed data file (:file:`dst`).

#. :code:`ana`: you analyze the reconstructed tracks and generate a :code:`CERN
   ROOT <https://root.cern.ch/root/htmldoc/guides/users-guide/InputOutput.html>`
   file containing trees that describe event and track variables
   (:code:`root`).

When you are analyzing measurement data, you won't have to perform steps 1 and
2: the BESIII collaboration reconstructs all data samples whenever a new
version of BOSS is released. (See :doc:`Organization of the IHEP server
</tutorials/getting-started/jobs>`, under "Reconstructed data sets", for where
these files are located.)

The steps are performed from :code:`jobOptions*.txt` files of your own package
in your work area. What is a job options file? Job options contain parameters
that are loaded by the algorithm of your package at run-time (have a look at
:code:`declareProperty` in the :doc:`RhopiAlg
</packages/analysis/examples/RhopiAlg>`). These parameters can be an output
file name, certain cuts, boolean switches for whether or not to write certain
NTuples, etc.

A job is run using the :code:`boss.exe` command,  with the path to a job option
file as argument. You can use the example job option files in
:code:`TestRelease` as a try:

.. code-block:: bash

  cd "$TESTRELEASEROOT/run/"
  boss.exe jobOptions_sim.txt
  boss.exe jobOptions_rec.txt
  boss.exe jobOptions_ana_rhopi.txt

This is essentially it! Of course, for your own analysis, you will have to
tweak the parameters in these :code:`jobOptions_*.txt` files and in
:code:`TestRelease` to integrate and run your own packages.

In the following, we will go through some extra tricks that you will need to
master in order to do computational intensive analyzes using **BOSS**.

.. admonition:: Analyzing all events

  In data analysis, you usually want to use all events available: cuts are
  applied to get rid of events you don't want. It is therefore better to use
  :code:`-1` , which stands for ' *all* events', for the maximum number of
  events in :code:`ApplicationMgr.EvtMax`.

Submitting a job
----------------

The :code:`TestRelease` package typically simulates, reconstructs, and analyzes
only a few hundred events. For serious work, you will have to generate
thousands of events and this will take a long time. You can therefore submit
your job to a so-called 'queue'. For this, there are two options: either you
submit them using the command :code:`hep_sub` or using the command
:code:`boss.condor`. The latter is easiest: you can use it just like
:code:`boss.exe`.

With :code:`hep_sub` , however, you essentially forward a shell script to the
queue, which then executes the commands in there. So you will **first put the
command for your job in make a shell script** (:code:`.sh`). Let's say, you
make a shell script :code:`test.sh` in the :code:`run` folder that looks like
this:

.. code-block:: bash

  #!/bin/bash
  boss.exe jobOptions_sim.txt

The first line clarifies that you use :code:`bash` , the second does what you
did when running a job: calling :code:`boss.exe` , but of course, you can make
this script to execute whatever :code:`bash` commands you want.

The 'queue' (:code:`hep_sub`) executes bash scripts using :code:`./` , not the
command :code:`bash`. You therefore have to make the script executable. This is
done through :code:`chmod +x <your_script>.sh` ('change mode to executable').

Now you can submit the shell script to the queue using:

.. code-block:: bash

  hep_sub -g physics test.sh

and your job will be executed by the computing centre. Here, the option
:code:`-g` tells that you are from the :code:`physics` group. A (more or less)
equivalent to this command is :code:`boss.condor test.sh`.

You can check whether the job is (still) running in the queue using:

.. code-block:: bash

  hep_q -u $USER

Note that :code:`hep_q` would list all jobs from all users. The first column of
the table you see here (if you have submitted any jobs) is the job ID. If you
have made some mistake in your analysis code, you can use this ID to **remove a
job** , like this:

.. code-block:: bash

  hep_rm 26345898.0

Alternatively, you can remove *all* your jobs from the queue using
:code:`hep_rm -a`.

Splitting up jobs
-----------------

Jobs that take a long time to be executed in the queue will be killed by the
server. It is therefore recommended that you work with a maximum of **10,000
events** per job if you perform Monte Carlo simulations (the :code:`sim` step
consumes much computer power). Of course, you will be wanting to work with much
larger data samples, sou you will have to submit parallel jobs. This can be
done by writing different :code:`jobOptions*.txt` files, where you modify the
input/output files and random seed number.

You can do all this by hand, but it is much more convenient to generate these
files with some script (whether C++, bash or :code:`tcsh`) that can generate
:code:`jobOptions*.txt` files from a certain *template file*. In these, you for
instance replace the specific paths and seed number you used by generic tokens
like :code:`INPUT_FILE` , :code:`OUTPUT_FILE` , and :code:`RANDOM_SEED`. You
can then use the script to replace these unique tokens by a path or a unique
number. Have a look at the `awk <https://www.tldp.org/LDP/abs/html/awk.html>`_
and `sed <https://www.gnu.org/software/sed/manual/sed.html>`_ commands to get
the idea.

Splitting scripts using the BOSS Job Submitter
----------------------------------------------

See `documentation of the BOSS Job Submitter repository
<https://github.com/redeboer/BOSS_JobSubmitter>`_.
