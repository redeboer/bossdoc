<!-- cspell:ignore ESIII ffline oftware ystem Chengping Shen -->

# What is BOSS?

BOSS is the **B**ESIII **O**ffline **S**oftware **S**ystem with which all data
from the BESIII detector is processed and analyzed. As a data analyzer, you
will use BOSS to make an initial event selection and collision info that is
relevant for your analysis to an output ROOT file. In the final event
selection, you use that ROOT file to produce the relevant plots for your
analysis.

In this section, we will discuss the three most important components that form
BOSS:

- {ref}`tutorials/getting-started/intro:The Gaudi Framework`, which streamlines
  algorithms used in analyzes.

- {ref}`CMT <tutorials/getting-started/intro:Configuration Management Tool (CMT)>`,
  which is used to manage packages designed by different groups.

- {ref}`CVS <tutorials/getting-started/intro:Concurrent Versions System (CVS)>`,
  which is the version control system used to maintain BOSS.

BOSS has been built on several other external libraries. The source files and
binaries can be found here on the `lxslc` server:

```text
/cvmfs/bes3.ihep.ac.cn/bes3sw/ExternalLib/SLC6/ExternalLib
```

You can also have a look at the
[BOSS External Libraries repository](https://github.com/redeboer/BOSS_ExternalLibs)
and the documentation there.

## The Gaudi Framework

An event selection program usually consists of three steps:

1. **Initialize**. Here, you for instance load raw data and set some variables.

2. **Execute**. For each collision event, you for instance extract parameters
   from the tracks.

3. **Finalize**. You write the data you collected to an output file.

Gaudi utilizes that idea in the form of
[an `Algorithm` class](https://dayabay.bnl.gov/dox/GaudiKernel/html/classAlgorithm.html).
Your analysis is defined by deriving from this class and specifying what you
want to be performed in the `initialize`, `execute`, and `finalize` steps.

:::{note}

For up to date tutorials about Gaudi, see
[this GitBook by the LHCb collaboration](https://lhcb.github.io/developkit-lessons/first-development-steps/02a-gaudi-helloworld.html).
A small warning: LHCb runs analysis through Python, while BESIII jobs are run
through `boss.exe`. In addition, LHCb uses an extended version of the
`Algorithm` class,
[called GaudiAlgorithm](https://twiki.cern.ch/twiki/bin/view/LHCb/GaudiAlgorithm),
so the instructions cannot be replicated for BOSS.

:::

## Configuration Management Tool (CMT)

The BOSS analysis framework is organized according to the so-called
"package-oriented principle". The underlying idea is that in a software
framework that is developed by several people is best split up into several
packages that are each developed independently or in subgroups.

The task of the CMT is to streamline and checkout different versions of these
packages, that is,
[to name them automatically](http://polywww.in2p3.fr/activites/physique/glast/workbook/pages/cmtMRvcmt/defCMTpackage.htm)
based on content and modifications and to connect the packages to each other
(to manage dependencies). This is done in conjunction with CVS
({ref}`see below <tutorials/getting-started/intro:Concurrent Versions System (CVS)>`).
CMT additionally allows users to ascribe properties to the packages and their
constituents.

See for more information:

- [An accessible introduction to CMT](http://polywww.in2p3.fr/activites/physique/glast/workbook/pages/cmtMRvcmt/cmtIntroduction.htm)

- [Official website of CMT](http://www.cmtsite.net/) (partially French)

- [Official CMT Manual webpage](http://www.cmtsite.net/CMTDoc.html)

- [LHCb on CMT](https://lhcb-comp.web.cern.ch/lhcb-comp/support/CMT/cmt.htm)
  (historical page)

## Concurrent Versions System (CVS)

Packages and source code of BOSS are monitored and maintained by CVS. This is a
revision control system comparable to Subversion and Git.

More information:

- [An accessible introduction to CVS](http://polywww.in2p3.fr/activites/physique/glast/workbook/pages/softwareOverview/cvsBasics.htm)

- [Commonly used CVS commands](http://polywww.in2p3.fr/activites/physique/glast/workbook/pages/softwareOverview/commonCVScommands.htm)

- [Wikipedia on CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System)
