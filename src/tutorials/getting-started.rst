Getting started with BOSS
=========================

This part of the tutorial focuses on setting up your BOSS environment on the IHEP server. It is essential to follow these steps if you haven't already done so, but you can also just browse through these steps to see if you missed anything. These tutorial pages also aim at providing more context about what you are actually doing, so they can also be useful if you are not a beginner.

Contents
--------

* :doc:`The role of the IHEP server <getting-started/server>` (:code:`lxslc`), where we explain the structure of the IHEP server, how to access it, and go through the directories that are most important to BOSS.

* :doc:`What is BOSS? <getting-started/intro>` Here, we go through some of the key ingredients of the BOSS framework, such as CMT and Gaudi.

* :doc:`Setup of your BOSS environment <getting-started/setup>` A step-by-step guide that explains you how to 'install' BOSS.

* :doc:`Set up a BOSS package <getting-started/setup-package>`, where we go through the mechanisms of CMT used to create, configure, and broadcast a BOSS package.

* :doc:`Running jobs <getting-started/jobs>` In this part, we will explain the :code:`boss.exe` mechanism, used to run an analysis package as a job.

* :doc:`Summary <getting-started/summary>` Finally, we will give a practical overview of the steps you usually go through when debugging an analysis package and submitting a corresponding job.


.. toctree::
  :maxdepth: 1

  getting-started/server
  getting-started/data-quota
  getting-started/intro
  getting-started/setup
  getting-started/setup-package
  getting-started/jobs
  getting-started/summary
