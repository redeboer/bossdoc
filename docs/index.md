# BESIII Offline Software System

```{title} Welcome

```

[![GPLv3+ license](https://img.shields.io/badge/License-GPLv3+-blue.svg)](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
[![Documentation build status](https://readthedocs.org/projects/bes3/badge/?version=latest)](https://bes3.readthedocs.io)

:::{warning}

These pages and are **under development** and originate from
[the BOSS GitBook](https://besiii.gitbook.io/boss). Official documentation for
BOSS can be found
[here](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Main_Page).

:::

:::{note}

Feedback on these pages is very welcome! See {doc}`contribute` for more
details.

:::

This website describes the use of the BESIII Offline Software System (BOSS).
The pages started as a collection of notes, but now aim to serve several
purposes:

- Provide accessible and up-to-date **tutorials** on working with BOSS. These
  pages written as step-by-step guides and are particularly aimed at beginners,
  but also provide background information of what the software is doing.

- Serve as an **inventory of packages** and libraries often used within BOSS.
  Ideally, this should allow analyzers to navigate through the tools that are
  already available.

- Serve as a platform where analyzers can **easily and continuously update**
  their documentation.

- Maintain an **updated list of references** to must-read web pages or
  literature on BESIII.

What goes for all of the above is that, whatever your background or level,
**your feedback is vital**, because these tutorial pages need testing and
improvement. More importantly, the more people contribute, the more these pages
can become a source of reference and are more likely to remain up-to-date.

So if you read this and like the idea, have a look at the {doc}`contribute`!
Contributions from all levels is highly appreciated.

```{hint}
If you do not have an IHEP networking account, it is better to check out the
official
[Offline Software page](http://english.ihep.cas.cn/bes/doc/2247.html) of
BESIII. For this, you in turn need to be a BESIII member and have an SSO
account, which can be done
[here](http://afsapply.ihep.ac.cn/cchelp/en/accounts/#21-user-account-application).

BOSS can only be of use if you are a member of the BESIII collaboration and if
you have access to the software of this collaboration. You can also have a look
at the links in the section {doc}`appendices/references`.
```

```{rubric} Contents of the tutorial pages

```

Here are shortcuts that you might want to take:

1. {doc}`Getting started with BOSS <tutorials/getting-started>`. If you are not
   familiar with BOSS, it is best to start with this part of the tutorial. It
   will help you set up the BOSS environment in your account on the IHEP server
   ('install BOSS'), explain you some basics of the package structure on which
   BOSS is built, and guide you through the process of submitting jobs.

2. {doc}`Major BOSS packages </packages>`. Here, you will find descriptions of
   some of the important BOSS packages used in initial event selection, most
   notably, the `RhopiAlg` package. This section is to serve as an inventory of
   BOSS packages.

3. {doc}`Physics at BESIII <physics>`. An inventory of important physics
   principles behind of data analysis at BESIII.

   ```{todo}
   _(These pages have not yet been written.)_
   ```

4. {doc}`Tips, Tricks, and Troubleshooting <appendices>`. These pages are used
   to collect problems that are frequently encountered when working with BOSS.
   As such, these notes are useful no matter your level. _New suggestions are
   most welcome!_

```{toctree}
---
maxdepth: 1
hidden: true
---
bes3
tutorials
packages
physics
appendices
contribute
```
