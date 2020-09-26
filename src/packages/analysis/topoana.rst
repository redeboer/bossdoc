.. cspell:ignore Ctruth Xingyu Zhou zhouxy

.. include:: /global.inc

TopoAna
=======

.. note::
  *Credit for the package goes to Zhou Xingyu* |br|
  For more information, see the `corresponding paper on arXiv <https://arxiv.org/abs/2001.04016>`_.

This package is an extremely helpful tool for analyzing the topologies of :term:`Inclusive Monte Carlo simulation`. Inclusive MC samples give us valuable information about the **background** of your analysis, as it allows you to know the true contributions to that background. If you know what components that background exists of, you can:


* try to make smart cuts to remove those background components;
* use a particular function that describes that background component best when applying a fit to the real data.

The problem with inclusive samples, however, is that they can include thousands of decay modes. The :code:`topoana` package allows you to make certain selections and to generate tables that list frequencies of particles and decay modes that are of interest to you.

All versions of the package can be found here on :ref:`the IHEP server <tutorials/getting-started/server:Accessing the server>`:

.. code-block:: text

   /besfs/users/zhouxy/tools/topoana

Preparing initial event selection
---------------------------------

The :code:`topoana` package has to be run over a ROOT file that you have to prepare yourself. The ROOT file has to contain a :code:`TTree` with specific information of the Monte Carlo truth:


* the **run ID** number
* the **event ID** number
* the **number of particles** in this event, which is necessary for loading the following arrays
* an array contain the **PDG code for each track** in this event
* an array containing the PDG code for the **mother of each track** (if available)

You can design a procedure to write this MC truth information yourself, but you can also use either of the following two methods:


#. Add the :code:`MctruthForTopo` algorithm package (see below) to the job options of your analysis.
#. Go through the code of the :code:`MctruthForTopo` algorithm and take over the relevant components in your own initial event selection package, so that you can implement it within your cut procedure.
#. Use the :code:`CreateMCtruthCollection` and :code:`WriteMcTruthForTopoAna` in the :code:`TrackSelector` base algorithm.

The :code:`MctruthForTopo` package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:code:`MctruthForTopo` is an example package that comes with :code:`topoana`. It can be used for preparing a ROOT file sample that contains a :code:`TTree` as described above. See the documentation of :code:`MctruthForTopo` for how these branches are typically called within :code:`MctruthForTopo-00-00-06`.

.. list-table::
   :header-rows: 1

   * - Version
     - Data type
   * - :code:`00-00-01`
     - No selection: all :code:`McParticle` s are loaded
   * - :code:`00-00-02`
     - Particles that don't come from a generator are rejected (`decayFromGenerator <http://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#675a3679ea082c13d4ca4ce1c5571b59>`_)
   * - :code:`00-00-03`
     - Specifically designed for :math:`J/\psi`
   * - :code:`00-00-04`
     - :math:`J/\psi`, but with bug fix for :code:`cluster` and :code:`string`
   * - :code:`00-00-05`
     - Designed for PID :math:`90022` and :math:`80022` (??)
   * - :code:`00-00-06`
     - :math:`4,180` MeV data


All versions of :code:`MctruthForTopo` can be found here on the IHEP server:

.. code-block:: bash

   /besfs/users/zhouxy/workarea/workarea-6.6.5/Analysis/Physics/MctruthForTopoAnaAlg

You may choose a different version of BOSS than :code:`6.6.5` , the one used above. If you have sourced one of these versions (using :code:`bash cmt/setup`), you can run it by adding the following lines to your job options:

.. code-block:: text

   ApplicationMgr.DLLs += {"MctruthForTopoAnaAlg"};
   ApplicationMgr.TopAlg += {"MctruthForTopoAna"};

Note: Using :code:`MctruthForTopoAna` is the quickest way to create a :code:`TTree` containing the necessary data for :code:`topoana` , but it does not allow you to perform cuts: **all the events** will be written to the :code:`TTree` and no cut will be applied.

Structure of the :code:`Event::McParticleCol` collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :code:`TTree` containing Monte Carlo data that is needed for :code:`topoana` is created by looping over the `Event::McParticleCol <http://bes3.to.infn.it/Boss/7.0.2/html/namespaceEvent.html#b6a28637c54f890ed93d8fd13d5021ed>`_ in each event and writing the branches described above. To gain a better understanding of what a package like :code:`MctruthForTopo` does, let's have a look at the the contents of the MC truth particle collection in one event:

.. list-table::
   :header-rows: 1

   * - Index
     - Particle
     -
     -
     - Index
     - Mother
     -
     -
   * - **0**
     - 23
     - :code:`Z0`
     - :math:`Z^0`
     -
     -
     -
     -
   * - **1**
     - 22
     - :code:`gamma`
     - :math:`\gamma`
     -
     -
     -
     -
   * - **2**
     - 4
     - :code:`c`
     - :math:`c`
     - **0**
     - 23
     - :code:`Z0`
     - :math:`Z^0`
   * - **3**
     - -4
     - :code:`anti-c`
     - :math:`\bar{c}`
     - **0**
     - 23
     - :code:`Z0`
     - :math:`Z^0`
   * - **4**
     - 91
     - :code:`cluster`
     -
     - **3**
     - -4
     - :code:`anti-c`
     - :math:`\bar{c}`
   * - **5**
     - 443
     - :code:`J/psi`
     - :math:`J/\psi`
     - **4**
     - 91
     - :code:`cluster`
     -
   * - **6**
     - 11
     - :code:`e-`
     - :math:`e^-`
     -
     -
     -
     -
   * - **7**
     - 421
     - :code:`D0`
     - :math:`D^0`
     - **5**
     - 443
     - :code:`J/psi`
     - :math:`J/\psi`
   * - **8**
     - 333
     - :code:`phi`
     - :math:`\phi`
     - **5**
     - 443
     - :code:`J/psi`
     - :math:`J/\psi`
   * - **9**
     - -321
     - :code:`K-`
     - :math:`K^-`
     - **7**
     - 421
     - :code:`D0`
     - :math:`D^0`
   * - **10**
     - 221
     - :code:`pi+`
     - :math:`\pi^+`
     - **7**
     - 421
     - :code:`D0`
     - :math:`D^0`
   * - **11**
     - 321
     - :code:`K+`
     - :math:`K^+`
     - **8**
     - 333
     - :code:`phi`
     - :math:`\phi`
   * - **12**
     - -321
     - :code:`K-`
     - :math:`K^-`
     - **8**
     - 333
     - :code:`phi`
     - :math:`\phi`
   * - **13**
     - -13
     - :code:`mu+`
     - :math:`\mu^+`
     - **11**
     - 321
     - :code:`K+`
     - :math:`K^+`
   * - **14**
     - 14
     - :code:`nu_mu`
     - :math:`\nu_\mu`
     - **11**
     - 321
     - :code:`K+`
     - :math:`K^+`
   * - **15**
     - -11
     - :code:`e+`
     - :math:`e^+`
     - **13**
     - -13
     - :code:`mu+`
     - :math:`\mu^+`
   * - **16**
     - 12
     - :code:`nu_e`
     - :math:`\nu_e`
     - **13**
     - -13
     - :code:`mu+`
     - :math:`\mu^+`
   * - **17**
     - -14
     - :code:`anti-nu_mu`
     - :math:`\bar{\nu}_{\mu}`
     - **13**
     - -13
     - :code:`mu+`
     - :math:`\mu^+`


A few remarks about what we see here:



#. The structure of the decay chain is described by the index (see `Event::McParticle::trackIndex <http://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#34dae94b0ed5f36b875f783e61f8efc9>`_). Each particle is labeled by this index and if there is a mother particle, it is 'linked' to its daughter by its index.

#. The decay chain starts with index :code:`0` , a :math:`Z^0` boson that emerges right after the :math:`e^+e^-` collision, which then decays into a :math:`c\bar{c}` charm pair. In the simulation, this pair is taken to be a :code:`cluster` (which has code :code:`91`) or a :code:`string` (which has code :code:`92`).

#. For :code:`TopoAna` (or actually any physics analysis), we are only interested in what happens after the formation of the cluster. This is where the meson is created to which the beam energy is tuned, in this case :math:`J/\psi`. **We therefore only store particles that come after either particle code 91 or 92** , see :code:`MctruthForTopoAna::execute`.

#. From the remainder of the table, we can see that the rest of the decay chain becomes (a rather rare if not impossible decay):

$$
J/\psi \rightarrow D^0 \phi \
D^0 \rightarrow K^-\eta \
\phi \rightarrow K^+K^- \
K^+ \rightarrow \mu^+\nu_\mu \
\mu^+ \rightarrow e^+\nu *e\bar{\nu}* \mu
$$

The main takeaway is that :code:`topoana` requires you to store the branch with "track index" :ref:`defined above <packages/analysis/topoana:Preparing initial event selection>` as **having an offset** : the first particle is to be the initial meson (e.g. :math:`J/\psi`) with track index :code:`0` , so that you can use the mother index as an array index. So you need to subtract its original index from index of the the particles that come after. In addition, the selection of MC truth particles is only to contain:


* Particles that result from the initial cluster or string, that is, everything that in this case comes after :math:`J/\psi`.
* Only particles that come from the generator. This means they are not background simulated in the detectors and that that they were included in the decay chain from the generator. (See `Event::McParticle::decayFromGenerator <http://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#675a3679ea082c13d4ca4ce1c5571b59>`_.) In this case, this means that everything that comes after the decay of :math:`D^0` and :math:`\phi` is to be excluded, because the :math:`\mu^+` and :math:`K^+` decays take place outside the BESIII detector.
* Only particles that have a mother particle (is not `primaryParticle <http://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#f225ad5eb24b49e277349c3ec2dd297e>`_).

In table format, with these conventions, the result that should be stored for the :code:`topoana` package would be:

.. list-table::
   :header-rows: 1

   * - Array index
     - Particle
     -
     -
     - Array index
     - Mother
     -
     -
   * - **0**
     - 443
     - :code:`J/psi`
     - :math:`J/\psi`
     - **-1**
     - 91
     - :code:`cluster`
     -
   * - **2**
     - 421
     - :code:`D0`
     - :math:`D^0`
     - **0**
     - 443
     - :code:`J/psi`
     - :math:`J/\psi`
   * - **3**
     - 333
     - :code:`phi`
     - :math:`\phi`
     - **0**
     - 443
     - :code:`J/psi`
     - :math:`J/\psi`
   * - **4**
     - -321
     - :code:`K-`
     - :math:`K^-`
     - **2**
     - 421
     - :code:`D0`
     - :math:`D^0`
   * - **5**
     - 211
     - :code:`pi+`
     - :math:`\pi^+`
     - **2**
     - 421
     - :code:`D0`
     - :math:`D^0`
   * - **6**
     - 321
     - :code:`K+`
     - :math:`K^+`
     - **3**
     - 333
     - :code:`phi`
     - :math:`\phi`
   * - **7**
     - -321
     - :code:`K-`
     - :math:`K^-`
     - **3**
     - 333
     - :code:`phi`
     - :math:`\phi`


Installing topoana
------------------

Execute `setup.sh <http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/setup.sh>`_ and see the instructions there on how to source it. If you have done this, you can use the command :code:`topoana.exe` the output generated through the :ref:`previous step <packages/analysis/topoana:Preparing initial event selection>`.

Format of a topoana card
------------------------

If you have :ref:`prepared a ROOT file <packages/analysis/topoana:Preparing initial event selection>` and :ref:`installed topoana.exe <packages/analysis/topoana:Installing topoana>`, you can analyze the output. The :code:`topoana` package will generate some tables containing statistics of certain signal particles and signal decay modes. You can specify these signal particles and branches through a :code:`topoana` card and run the analysis with the command :code:`topoana.exe your_topoana.card`.

A :code:`topoana` card file (:file:`.card` extension) is a text file that defines the way in which you execute :code:`topoana.exe` on your data set. In this file, you for instance specify the input ROOT files that you want to analyze.

The syntax of the :code:`topoana` card is slightly reminiscent of :code:`bash`. Starting a line with:


* :code:`#` means that the line is a comment and is therefore ignored;
* :code:`%` means that the the line represents a field.

A opening curly brace (:code:`{`) following a :code:`%` sign means that a field block is opened. The next line(s) contain the value(s) of that field. Close the block with a closing curly brace (:code:`}`).

The following pages list **all fields** that can be used in your :code:`topoana` card: :doc:`required </packages/analysis/topoana/required>` and :doc:`optional fields </packages/analysis/topoana/optional>`.

Tips on the results
-------------------

*(From* :code:`topoana` *terminal output.)*


#. Statistics of the topologies are summarized in three types files: :code:`pdf` , :code:`tex` and :code:`txt`. Although these are different formats, they contain the same information. The :code:`pdf` file is the easiest to read. It has been converted from the :code:`tex` file using the :code:`pdflatex` command. If necessary, you can check the contents of the :code:`txt` file as well (e.g. using text processing commands).
#. Tags of the topologies are inserted in all the entries of :code:`TTree` for :code:`topoana` in the output ROOT file(s). The ROOT files may have been split up, in which case you should load them using a :code:`TChain`. Except for this, the :code:`TTree` for :code:`topoana` data of the output ROOT file is entirely the same as that of the input ROOT file(s). In addition, the topology tags are identical with those listed in the txt, tex, and pdf files.

Submitting a :code:`topoana.exe` job
------------------------------------

Just like a BOSS job, you can submit a :code:`topoana` job to the queue. This is useful if your data is extensive and you want to log out while the job is executed. Just write your command in a :code:`bash` script like this:

.. your_bash_file.sh

.. code-block:: bash

   { topoana.exe your_topoana.card; } &> your_file.log

The pipe (:code:`>`) with the curly braces ensures that all output (including warnings) is written to the log file (here, :code:`your_file.log`).

Make sure that you make the :code:`bash` script executable using :code:`chmod +x your_bash_file.sh`. You can then submit your job to the queue using:

.. code-block:: bash

   hep_sub -g physics your_bash_file.sh

and keep an eye on your jobs using:

.. code-block:: bash

   hep_q -u $USER


.. toctree::
  :maxdepth: 1

  topoana/required
  topoana/optional
