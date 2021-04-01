.. cspell:ignore maqm sysgroup


Set up your BOSS environment
============================

.. warning::
  In it's current version, this tutorial assumes you use a :code:`bash`
  terminal. It should work for TC-shell as well, but if you experience
  problems, please :doc:`contact me </contributing>`.

.. note::
  See :ref:`last section of this page <tutorials/getting-started/setup:Summary
  of commands>` for an overview of all commands. If you are in a very lazy
  mood, you can also download and run `this bash script
  <http://code.ihep.ac.cn/bes3/BOSS_StarterKit/-/tree/master/utilities/SetupBoss.sh>`_:

.. code-block:: bash

  wget https://raw.githubusercontent.com/redeboer/BOSS_StarterKit/master/utilities/SetupBoss.sh
  bash SetupBoss.sh


In this section, you will learn how to 'install' BOSS. Since BOSS has already
been compiled on the server, installing actually means that you set up *path
variables* in the :code:`bash` shell. Shortly said, your user account then
'knows' where to locate BOSS and how to run it.

There are two main directories that you will be using:

#. a *local install area* , from which access to BOSS is managed and which
   contains your own BOSS packages (mostly event selection), and

#. an *analysis folder* , which contains scripts that you design yourself to
   analyze output from BOSS (for example fitting histograms). You can decide to
   have this folder locally on your own pc, because analyzes of this type
   require less computing power.

It is totally up to you where you place these folders. A common procedure is to
put the *analysis folder* in the :code:`ihepbatch` folder. Have a look at the
:doc:`organization of the IHEP server </tutorials/getting-started/server>` to
decide if there is some other folder that meets your needs.

.. admonition:: In case of large data

  If you work with large data samples, you may want to write your output to a
  different folder in :ref:`scratchfs
  <tutorials/getting-started/server:Important data paths>`. Take care to modify
  the paths your job option files accordingly! (See :doc:`running jobs
  </tutorials/getting-started/jobs>`.)


Set up the BOSS environment
---------------------------

Step 1: Define your local install folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the sake of making this tutorial work in a general setting, we will first
define a :code:`bash` variable here (you can just execute this command in
:code:`bash`):

In this part of the tutorial, we will do two things: (1) setup the necessary
references to BOSS and (2) preparing your :code:`workarea` folder. You will be
developing and your own BOSS packages (mainly code for event selection) in this
:file:`workarea` folder. Next to your :file:`workarea` , there will be a
:ref:`Configuration Management Tool
<tutorials/getting-started/intro:Configuration Management Tool (CMT)>` folder
(:file:`cmthome`), which manages access to the BOSS installation. In the end
you will have a file structure like this:


* :file:`/besfs5/users/$USER/boss/` (local install area)

  * :file:`cmthome` (manages access to BOSS)
  * :file:`workarea` (contains your analysis code)

    * :file:`TestRelease` (loads essential BOSS packages)
    * :file:`InstallArea` (binaries and header files are collected here after
      compiling)

.. note::

  The above is equivalent to :code:`BOSS_INSTALL=/besfs5/users/$USER/boss` , so
  why the quotation marks (:code:`"..."`) and curly braces (:code:`{...}`)?
  It's just a good habit in :code:`bash` scripting to avoid bugs and improve
  readability. The quotation marks clarify that we are storing a string here
  and allow you to use spaces, while the curly braces clarify the extend of the
  variable name (:code:`USER` in this case).

.. code-block:: bash

  BOSS_INSTALL="/besfs5/users/${USER}/boss"

This variable points to the path that will contain your local 'install' of
BOSS. You can change what is between the quotation marks by whatever folder you
prefer in case you want your local BOSS install to be placed in some other
path, for instance by :code:`/ihepbatch/bes/$USER`.

At this stage, you'll have to decide which version of BOSS you have to use. At
the time of writing, **version 7.0.4** is the latest stable version, though it
could be that for your analysis you have to use data sets that were
reconstructed with older versions of BOSS. Here, we'll stick with :code:`7.0.4`
, but you can replace this number with whatever version you need.

For convenience, we'll again define the version number as a variable here.

.. code-block:: bash

  BOSS_VERSION="7.0.4"

.. tip::
  An overview of all BOSS versions and their release notes can be found `here <https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/ReleaseNotes>`_ (requires login).

Step 2: Import environment scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We first have to obtain some scripts that allow you to set up references to
BOSS. This is done by copying the :file:`cmthome` folder from the BOSS Software
directory, which contains all source code for BOSS, to your local install area
(option :code:`-p` allows :code:`mkdir` to work on arbitrary depth):

.. code-block:: bash

  mkdir -p "$BOSS_INSTALL/cmthome"
  cd "$BOSS_INSTALL/cmthome"
  cp -Rf /cvmfs/bes3.ihep.ac.cn/bes3sw/cmthome/cmthome-$BOSS_VERSION/* .

Note from the :code:`cp` command that we have omitted the version from the
original folder name. You can choose to keep that number as well, but here we
chose to use the convention is that :file:`cmthome` and :file:`workarea`
without a version number refers to the latest stable version of BOSS.

.. _Step 3:

Step 3: Modify :code:`requirements`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In :code:`cmthome*` , you now have to modify a file called :file:`requirements`
, so that it handles your username properly. We'll use the :code:`vi` editor
here, but you can use whatever editor you prefer:

.. code-block:: bash

  vi requirements

The file contains the following lines:

.. code-block:: bash

  #macro WorkArea "/ihepbatch/bes/maqm/workarea"

  #path_remove CMTPATH "${WorkArea}"
  #path_prepend CMTPATH "${WorkArea}"

Uncomment them (remove the hash :code:`#`) and replace what is between the
first quotation marks :code:`"..."` with your the path to your workarea. In our
case, it looks like this:

.. code-block:: bash

  macro WorkArea "/besfs5/users/$USER/boss/workarea"

  path_remove CMTPATH "${WorkArea}"
  path_prepend CMTPATH "${WorkArea}"

The :code:`$CMTPATH` is an important variable for :ref:`CMT
<tutorials/getting-started/intro:Configuration Management Tool (CMT)>`. It is
comparable to :code:`$PATH` in that it lists all directories that contain CMT
packages. Note that, when CMT searches for packages that you listed in the
:file:`requirements` file, it will use the first occurrence in the
:code:`$CMTPATH`. This is why you :code:`prepend` it.

**Step 4: Set references to BOSS**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now you can use the scripts in :file:`cmthome` to set all references to BOSS at
once, using:

.. code-block:: bash

  source setupCMT.sh  # starts connection to the CMT
  cmt config          # initiates configuration
  source setup.sh     # sets path variables

Just to be sure, you can check whether the path variables have been set
correctly:

.. code-block:: bash

  echo $CMTPATH

If everything went well, it should print something like:

.. code-block:: bash

  /besfs5/users/$USER/boss/workarea:/cvmfs/bes3.ihep.ac.cn/bes3sw/Boss/7.0.4:
  /cvmfs/bes3.ihep.ac.cn/bes3sw/ExternalLib/SLC6/ExternalLib/gaudi/GAUDI_v23r9:
  /cvmfs/bes3.ihep.ac.cn/bes3sw/ExternalLib/SLC6/ExternalLib/LCGCMT/LCGCMT_65a

The paths listed here (separated by :code:`:` columns) will be used to look for
packages required by the :file:`requirements` files of packages (see
:doc:`/tutorials/getting-started/setup-package`). The first of these paths
points to your :file:`workarea` , the second to the BOSS version you use (also
called :code:`$BesArea`), and the rest point to external libraries such as
`Gaudi <https://dayabay.bnl.gov/dox/GaudiKernel/html/annotated.html>`_.

Step 4: Create a :code:`workarea` sub-folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`As mentioned in the introduction <tutorials/getting-started/setup:Set up
the BOSS environment>`, the local install area contains a :code:`workarea`
folder next to the :file:`cmthome` folder we have been using so far. In our
case it will be:

.. code-block:: bash

  mkdir -p "$BOSS_WORKAREA/workarea"

We'll get back to the :code:`workarea` folder when we
:doc:`/tutorials/getting-started/setup-package`.

.. note::
  Your *BOSS workarea* typically contains three folders (see `an example here
  <http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea>`_):

  #. `Analysis
     <http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis>`_,
     which contains CMT packages that you use for your analysis

  #. `InstallArea
     <http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/InstallArea>`_,
     which is created when you use :code:`cmt config`

  #. `TestRelease
     <http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/TestRelease>`_,
     which is used to run all packages

  The file structure of your *workarea* follows that of the packages in
  :code:`$BesArea` (use :code:`ls $BesArea` to verify this), because, :ref:`as
  explained before <Step 3>`, packages in your *workarea* have priority over
  those in :code:`$BesArea`. As such, you can expand your *workarea* by copying
  certain packages from the :code:`$BesArea` and modifying those. In the *BOSS
  Afterburner* , there is for instance `a modification of the BesEvtGen Monte
  Carlo generator
  <http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Generator>`_.


.. _Step 5:

Step 5: Implement the :code:`TestRelease` package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BOSS is built up of a large number of packages, such as :code:`VertexFit`. Your
local account needs to load the essential ones in order for you to be able to
run the :file:`boss.exe` executable. For this, all versions of BOSS come with
the :code:`TestRelease` package. This package helps you to load those essential
packages.

Copy the latest :code:`TestRelease` package from the :code:`$BesArea` (where
the source code of the BOSS version you chose is located) to your
:file:`workarea` :

.. code-block:: bash

  cd $BOSS_INSTALL/workarea
  cp -Rf $BesArea/TestRelease .

Then move into the :code:`cmt` folder that comes with it and source scripts in
there:

.. code-block:: bash

  cd TestRelease/TestRelease-*/cmt
  cmt broadcast      # load all packages to which TestRelease refers
  cmt config         # perform setup and cleanup scripts
  cmt broadcast make # build executables
  source setup.sh    # set bash variables

.. _Step 6:

Step 6: Test BOSS using :code:`boss.exe`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To test whether everything went correctly, you can try to run BOSS:

.. code-block:: text

  boss.exe

It should result in a (trivial) error message like this:

.. code-block:: text

                 BOSS version: 7.0.4
  ************** BESIII Collaboration **************

  the jobOptions file is : jobOptions.txt
  ERROR! the jobOptions file is empty!

If not, something went wrong and you should carefully recheck what you did in
the above steps.

.. _step7:

Step 7: Modify your :file:`.bashrc`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to have the references to BOSS loaded automatically every time you log
in on the server, we can add some of the steps we did above to your
:code:`bash` profile (:file:`.bash_profile`) and *run commands* file
(:file:`.bashrc`).

.. note::
  On a *login terminal* , the :file:`.bash_profile` script is loaded every time
  you log in, while a *local terminal* (like a Ubuntu install on your own pc)
  loads :file:`.bashrc` (run commands). In the following, we therefore just
  'forward' the loading of :file:`.bash_profile` to :file:`.bash_rc`.

  First, add the following lines to your bash profile (use :code:`vi
  ~/.bash_profile`):


.. code-block:: bash
  :caption: .bash_profile

  if [[ -f ~/.bashrc ]]; then
    source ~/.bashrc
  fi

These lines force the server to source your :code:`.bashrc` run commands file
when you log in. In that file, you should add the following lines:

.. code-block:: bash
  :caption: .bashrc

  export BOSS_INSTALL="/besfs5/users/${USER}/boss"
  export BOSS_VERSION="7.0.4"
  CMTHOME="/cvmfs/bes3.ihep.ac.cn/bes3sw/cmthome/cmthome-${BOSS_VERSION}"

  source "${BOSS_INSTALL}/cmthome/setupCMT.sh"
  source "${BOSS_INSTALL}/cmthome/setup.sh"
  source "${BOSS_INSTALL}/workarea/TestRelease/TestRelease-*/cmt/setup.sh"
  export PATH=$PATH:/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/

Notice that the commands we used the previous steps appear here again. The last
line allows you to submit BOSS jobs to the 'queue' (using the :code:`hep_sub`
command) — for now, don't worry what this means.

To reload the run commands, either just log in again or use :code:`source
~/.bashrc`.

Summary of commands
-------------------

The following summarizes all commands required to 'install' BOSS on
:code:`lxslc` on your IHEP user account. If you don't know what you are doing,
go through the sections above to understand what's going on here.

.. code-block:: bash

  BOSS_INSTALL=/besfs5/users/$USER/boss
  BOSS_VERSION=7.0.4
  mkdir -p $BOSS_INSTALL/cmthome
  cd $BOSS_INSTALL/cmthome
  cp -Rf /cvmfs/bes3.ihep.ac.cn/bes3sw/cmthome/cmthome-$BOSS_VERSION/* .
  vi requirements

Now uncomment and change the lines containing :code:`WorkArea` to
:file:`/besfs5/users/$USER/boss/workarea`. Then:

.. code-block:: bash

  source setupCMT.sh
  cmt config
  source setup.sh
  mkdir -p $BOSS_INSTALL/workarea
  cd $BOSS_INSTALL/workarea
  cp -Rf $BesArea/TestRelease .
  cd TestRelease/TestRelease-*/cmt
  cmt broadcast      # load all packages to which TestRelease refers
  cmt config         # perform setup and cleanup scripts
  cmt broadcast make # build executables
  source setup.sh    # set bash variables

If you want, you can add the :code:`source` commands above your
:file:`.bash_profile` so that BOSS is sourced automatically setup scripts
automatically each time you log in. In simple copy-paste commands:

.. code-block:: bash

  OUT_FILE=~/.bash_profile
  echo >> $OUT_FILE
  echo "export BOSS_INSTALL=/besfs5/users/$USER/boss" >> $OUT_FILE
  echo "source \$BOSS_INSTALL/cmthome/setupCMT.sh"  >> $OUT_FILE
  echo "source \$BOSS_INSTALL/cmthome/setup.sh"  >> $OUT_FILE
  echo "source \$BOSS_INSTALL/workarea/TestRelease/TestRelease-*/cmt/setup.sh" >> $OUT_FILE
  echo "export PATH=\$PATH:/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin" >> $OUT_FILE
