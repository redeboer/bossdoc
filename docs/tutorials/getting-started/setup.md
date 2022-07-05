<!-- cspell:ignore maqm sysgroup -->

# Set up your BOSS environment

:::{warning}

In it's current version, this tutorial assumes you use a `bash` terminal. It should work
for TC-shell as well, but if you experience problems, please visit {doc}`/contribute` or
click the edit or issue buttons above!

:::

:::{tip}

See
{ref}`last section of this page <tutorials/getting-started/setup:Summary of commands>`
for an overview of all commands. If you are in a very lazy mood, you can also checkout
the [BOSS Starter Kit](http://code.ihep.ac.cn/bes3/BOSS_StarterKit), which this whole
set-up for you.

:::

In this section, you will learn how to 'install' BOSS. Since BOSS has already been
compiled on the server, installing actually means that you set up _path variables_ in
the `bash` shell. In short, your user account then 'knows' where to locate BOSS and how
to run it.

## Set up the BOSS environment

(step-1)=

### Step 1: Define your local install folder

In this part of the tutorial, we will do two things: (1) setup the necessary references
to BOSS and (2) preparing your `workarea` folder. You will be developing your own BOSS
packages (mainly code for event selection) in this `workarea` folder. Next to your
`workarea`, there will be a
{ref}`CMT <tutorials/getting-started/intro:Configuration Management Tool (CMT)>` folder
(`cmthome`), which manages access to the BOSS installation. In the end you will have a
file structure like this:

- `/besfs5/users/$USER/boss/` (local install area)

  - `cmthome` (manages access to BOSS)
  - `workarea` (contains your analysis code)

    - `MyEventSelectionPackage` (could be several packages)
    - `TestRelease` (loads and checks essential BOSS packages)
    - `InstallArea` (binaries and header files are collected here after compiling)

For the sake of making this tutorial work in a general setting, we will first define a
`bash` variable here (you can just execute this command in `bash`):

```bash
BOSS_INSTALL="/besfs5/users/${USER}/boss"
```

:::{toggle}

The above is equivalent to

```bash
BOSS_INSTALL=/besfs5/users/$USER/boss
```

Why the quotation marks (`"..."`) and curly braces (`{...}`)? It's just a good habit in
`bash` scripting to avoid bugs and improve readability. The quotation marks ensure that
we are storing a string here and allow you to use spaces, while the curly braces clarify
the extend of the variable name (`USER` in this case).

:::

This variable points to the path that will contain your local 'install' of BOSS. You can
change what is between the quotation marks by whatever folder you prefer, in case you
want your local BOSS install to be placed in some other path, for instance by
`/ihepbatch/bes/$USER`.

At this stage, you'll have to decide which version of BOSS you have to use. At the time
of writing, **version 7.0.5** is the latest stable version, though it could be that for
your analysis you have to use data sets that were reconstructed with older versions of
BOSS. Here, we'll stick with `7.0.5`, but you can replace this number with whatever
version you need.

For convenience, we'll again define the version number as a variable here.

```bash
BOSS_VERSION="7.0.5"
```

:::{tip}

An overview of all BOSS versions and their release notes can be found
[here](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/ReleaseNotes) (requires
login).

:::

(step-2)=

### Step 2: Import environment scripts

We first have to obtain some scripts that allow you to set up references to BOSS. This
is done by copying the `cmthome` folder from the BOSS Software directory (which contains
all source code for BOSS) to your local install area

:::{margin}

Option `-p` makes `mkdir` work on arbitrary depth and ignores existing directories

:::

```bash
mkdir -p "$BOSS_INSTALL/cmthome"
cd "$BOSS_INSTALL/cmthome"
cp -Rf /cvmfs/bes3.ihep.ac.cn/bes3sw/cmthome/cmthome-$BOSS_VERSION/* .
```

Note that we have omitted the version from the original folder name. You can choose to
keep that number as well, but here we chose to use the convention that `cmthome` and
`workarea` without a version number refers to the latest stable version of BOSS.

(step-3)=

### Step 3: Modify `requirements`

In `cmthome*`, you now have to modify a file called `requirements`, so that it handles
your username properly. We'll use the `vi` editor here, but you can use whatever editor
you prefer:

```bash
vi requirements
```

The file contains the following lines:

```bash
macro WorkArea "/ihepbatch/bes/maqm/workarea"

path_remove CMTPATH "${WorkArea}"
path_prepend CMTPATH "${WorkArea}"
```

The first line needs to be modified so that the variable `${WorkArea}` points to your
quotation marks with the path to your workarea. In our case, the first line becomes:

```bash
macro WorkArea "/besfs5/users/$USER/boss/workarea"
```

:::{dropdown} What is this `requirements` file actually?

A `requirements` file is used by CMT and is written in a syntax that CMT understands.
For instance, `path_remove` let's CMT removes the value of `"${WorkArea}"` from the
variable `$CMTPATH` (a `:`-separated list!). Next, `path_prepend` prepends the value
`"${WorkArea}"` back to that same `$CMTPATH` list.

The `$CMTPATH` is an important variable for
{ref}`CMT <tutorials/getting-started/intro:Configuration Management Tool (CMT)>`. It is
comparable to `$PATH` in that it lists all directories that contain CMT packages. When
CMT searches, it will start by searching in the first directory listed under `$CMTPATH`.
Since you want your own packages in your `$WorkArea` to supersede those of the BOSS
installation, you `path_prepend` it.

:::

### Step 4: Set references to BOSS

Now you can use the scripts in `cmthome` to set all references to BOSS at once, using:

```bash
source setupCMT.sh  # starts connection to the CMT
cmt config          # initiates configuration
source setup.sh     # sets path variables
```

Just to be sure, you can check whether the path variables have been set correctly:

```bash
echo $CMTPATH
```

If everything went well, it should print something like:

```bash
/besfs5/users/$USER/boss/workarea:
/cvmfs/bes3.ihep.ac.cn/bes3sw/Boss/7.0.5:
/cvmfs/bes3.ihep.ac.cn/bes3sw/ExternalLib/SLC6/ExternalLib/gaudi/GAUDI_v23r9:
/cvmfs/bes3.ihep.ac.cn/bes3sw/ExternalLib/SLC6/ExternalLib/LCGCMT/LCGCMT_65a
```

The paths listed here (separated by `:` columns) will be used to look for packages
required by the `requirements` files of packages (see
{doc}`/tutorials/getting-started/setup-package`). The first of these paths points to
your `workarea`, the second to the BOSS version you use (also called `$BesArea`), and
the rest point to external libraries such as
[Gaudi](https://dayabay.bnl.gov/dox/GaudiKernel/html/annotated.html).

(step-5)=

### Step 5: Create a `workarea` sub-folder

As mentioned in {ref}`tutorials/getting-started/setup:Set up the BOSS environment`, the
local install area contains a `workarea` folder next to the `cmthome` folder we have
been using so far. In our case, it will be:

```bash
mkdir -p "${BOSS_INSTALL}/workarea"
```

We'll get back to the `workarea` folder when we
{doc}`/tutorials/getting-started/setup-package`.

(step-6)=

### Step 6: Implement the `TestRelease` package

BOSS is built up of a large number of packages, such as `VertexFit`. Your local account
needs to load the essential ones in order for you to be able to run the `boss.exe`
executable. For this, all versions of BOSS come with the `TestRelease` package. This
package helps you to load those essential packages.

Copy the latest `TestRelease` package from the `$BesArea` (where the source code of the
BOSS version you chose is located) to your `workarea`:

```bash
cd $BOSS_INSTALL/workarea
cp -Rf $BesArea/TestRelease .
```

Then move into the `cmt` folder that comes with it and source scripts in there:

```bash
cd TestRelease/TestRelease-*/cmt
cmt broadcast      # load all packages to which TestRelease refers
cmt config         # perform setup and cleanup scripts
cmt broadcast make # build executables
source setup.sh    # set bash variables
```

(step-7)=

### Step 7: Test BOSS using `boss.exe`

To test whether everything went correctly, you can try to run BOSS:

```text
boss.exe
```

It should result in a (trivial) error message like this:

```text
              BOSS version: 7.0.5
************** BESIII Collaboration **************

the jobOptions file is: jobOptions.txt
ERROR! the jobOptions file is empty!
```

If not, something went wrong and you should carefully recheck what you did in the above
steps.

(step-8)=

### Step 8: Modify your `.bashrc`

In order to have the references to BOSS loaded automatically every time you log in on
the server, we can add some of the steps we did above to your `bash` profile
(`.bash_profile`) and _run commands_ file (`.bashrc`).

:::{margin}

<!-- cspell:ignore ommands -->

On a _login terminal_, the `.bash_profile` script is loaded every time you log in, while
a _local terminal_ (like Ubuntu on your own pc) loads `.bashrc` (`r`un `c`ommands).
Here, we therefore just 'forward' the loading of `.bash_profile` to `.bash_rc`.

:::

First, add the following lines to your bash profile (use `vi ~/.bash_profile`):

```{code-block} bash
:caption: .bash_profile
if [[ -f ~/.bashrc ]]; then
  source ~/.bashrc
fi
```

These lines force the server to source your `.bashrc` run commands file when you log in.
In that file, you should add the following lines:

```{code-block} bash
:caption: .bashrc
export BOSS_INSTALL="/besfs5/users/${USER}/boss"
export BOSS_VERSION="7.0.5"
CMTHOME="/cvmfs/bes3.ihep.ac.cn/bes3sw/cmthome/cmthome-${BOSS_VERSION}"

source "${BOSS_INSTALL}/cmthome/setupCMT.sh"
source "${BOSS_INSTALL}/cmthome/setup.sh"
source "${BOSS_INSTALL}/workarea/TestRelease/TestRelease-"*"/cmt/setup.sh"
export PATH=$PATH:/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/
```

Notice that the commands we used the previous steps appear here again. The last line
allows you to submit BOSS jobs to the 'queue' (using the `hep_sub` command) — for now,
don't worry what this means.

To reload the run commands, either just log in again or use `source ~/.bashrc`.

## Summary of commands

The following summarizes all commands required to 'install' BOSS on `lxslc` on your IHEP
user account. If you don't know what you are doing, go through the sections above to
understand what's going on here.

```bash
BOSS_INSTALL=/besfs5/users/$USER/boss
BOSS_VERSION=7.0.5
mkdir -p $BOSS_INSTALL/cmthome
cd $BOSS_INSTALL/cmthome
cp -Rf /cvmfs/bes3.ihep.ac.cn/bes3sw/cmthome/cmthome-$BOSS_VERSION/* .
vi requirements
```

Now uncomment and change the lines containing `WorkArea` to
`/besfs5/users/$USER/boss/workarea`. Then:

```bash
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
```

If you want, you can add the `source` commands above your `.bash_profile` so that BOSS
is sourced automatically setup scripts automatically each time you log in. In simple
copy-paste commands:

```bash
OUT_FILE=~/.bash_profile
echo >> $OUT_FILE
echo "export BOSS_INSTALL=/besfs5/users/$USER/boss" >> $OUT_FILE
echo "source \$BOSS_INSTALL/cmthome/setupCMT.sh"  >> $OUT_FILE
echo "source \$BOSS_INSTALL/cmthome/setup.sh"  >> $OUT_FILE
echo "source \$BOSS_INSTALL/workarea/TestRelease/TestRelease-*/cmt/setup.sh" >> $OUT_FILE
echo "export PATH=\$PATH:/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin" >> $OUT_FILE
```
