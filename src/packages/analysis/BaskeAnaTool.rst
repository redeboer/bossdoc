.. cspell:ignore addcut Baske dirdirectory Hepsub

.. include:: /global.inc

BaskeAnaTool
============

"BaskeAnaTool" means a basket of ana useful tools. You can use it to submit jobs to the computer servers, also generate simulation jobs, check the jobs status, check the whether the jobs is successful according to the job log files.

The package based on Python works independent of BOSS, but facilitates for instance MC simulation. The package can be obtained from GitHub: |br|
`https://github.com/xxmawhu/BaskeAnaTool <https://github.com/xxmawhu/BaskeAnaTool>`_

Before using the package, I suggest you to read the "Readme" carefully. The Chinese version of "Readme" is also available now.

How to install
--------------

First, you need to clone the repository from "github.com"

.. code-block:: bash

   git clone https://github.com/xxmawhu/BaskeAnaTool.git

The environment configuration is set well in the "setup.sh", you need to source it.

.. code-block:: bash

      source BaskeAnaTool/setup.sh

For the shell with tcsh users, there is one "setup.csh" file achieving same effect.

.. code-block:: bash

      source BaskeAnaTool/setup.csh

What does the basket contain?
-----------------------------


* submit jobs flexible

..

   For example, assuming you are now at directory "jobs", after "ls", you find many jobs need to be submitted.

   .. code-block:: bash

      jobs_ana_001.txt jobs_ana_004.txt jobs_ana_007.txt jobs_ana_010.txt
      jobs_ana_002.txt jobs_ana_005.txt jobs_ana_008.txt jobs_ana_011.txt
      jobs_ana_003.txt jobs_ana_006.txt jobs_ana_009.txt jobs_ana_012.txt

   Now, you only need one command

   .. code-block:: bash

      Hepsub -txt *.txt

   If you find many jobs allocated in different directories at the "jobs". Also one command is enough

   .. code-block:: bash

      Hepsub -txt -r .

   Don't forget to ".", which denotes the current directory. You also can specify the file type, execute method, and submit way.

   .. code-block:: bash

      Hepsub type="C, Cpp, cxx" exe="root -l -b -q" sub="hep_sub -g physics"

   Look into `https://github.com/xxmawhu/BaskeAnaTool <https://github.com/xxmawhu/BaskeAnaTool>`_ for more details.



*
  Do MC simulation flexible

  ..

     The following command is typically usage.

     .. code-block:: bash

        SimJpsi [decay.card] [number of events]

     You can enjoy the physics and forget all dirty bash script!


..

   How to DIY one? Write the following into one file, for example "doSim.py"

   .. code-block:: python

      #!/usr/env python
      import SimAndRec
      from SimAndRec import util
      svc = SimAndRec.process("sim.txt","rec.txt")
      if len(util.getArv()) == 0:
          svc.Make()
          svc.Sub()
      elif '-make' in util.getArv():
          svc.Make()

   The you can use "doSim.py" now

   .. code-block:: text

      python doSim.py [decay.card] [number of events]

   I also suggest you push "alias SimDIY='python /path/to/doSim.py'", into your configuration file, once you use "doSim.py frequently. Look into BaskeAnaTool/SimAndRec/gen.py for simpler way to generate your DIY command.


   *
     generate and submit typically BOSS event selection jobs

     There is one class "ana" in module "Bes". Main features:

     .. code-block:: python

        setJobOption()
        addDataSet()
        addcut()
        make()
        sub()

     You can find some examples in the dirdirectory "BaskeAnaTool/tutorials"

     Running "ana_Psi2S_inc.py", feeling it more directly.
