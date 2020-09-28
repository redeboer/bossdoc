.. title:: Welcome

BESIII Offline Software System
==============================

.. include:: global.inc

.. list-table::

  * - .. image:: https://readthedocs.org/projects/bes3/badge/?version=latest
        :alt: Documentation build status
        :target: https://bes3.readthedocs.io/en/latest/

      .. image:: https://img.shields.io/badge/License-GPLv3+-blue.svg
        :alt: GPLv3+ license
        :target: https://www.gnu.org/licenses/gpl-3.0-standalone.html

  * - .. image:: https://github.com/redeboer/bossdoc/workflows/CI/badge.svg
        :alt: CI status
        :target: https://github.com/redeboer/bossdoc/actions?query=branch%3Amaster+workflow%3A%22CI%22

      .. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
        :target: https://github.com/pre-commit/pre-commit
        :alt: pre-commit

      .. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :alt: Code style: black
        :target: https://github.com/psf/black

      .. image:: https://camo.githubusercontent.com/687a8ae8d15f9409617d2cc5a30292a884f6813a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64655f7374796c652d70726574746965722d6666363962342e7376673f7374796c653d666c61742d737175617265
        :alt: Code style: Prettier
        :target: https://prettier.io

.. warning::
  These pages and are **under development** and originate from `the BOSS
  GitBook <https://besiii.gitbook.io/boss>`_.

.. note::
  Feedback on these pages is very welcome! See :doc:`contributing` for contact details.

This GitBook describes the use of the BESIII Offline Software System (BOSS).
These pages started as a collection of notes, but now aim to serve several
purposes:

* Provide accessible and up-to-date **tutorials** on working with BOSS. These
  pages written as step-by-step guides and are particularly aimed at beginners,
  but also provide background information of what the software is doing.

* Serve as an **inventory of packages** and libraries often used within BOSS.
  Ideally, this should allow analyzers to navigate through the tools that are
  already available.

* Serve as a platform where analyzers can **easily and continuously update**
  their documentation.

* Maintain an **updated list of references** to must-read web pages or
  literature on BESIII.

What goes for all of the above is that, whatever your background or level,
***your feedback is vital**. These tutorial pages are quite new and need
testing and improvement. More importantly, the more people contribute, the more
these pages can become a source of reference and are more likely to remain
up-to-date.

So if you read this and like the idea, have a look at the :doc:`contributing
page <contributing>`! Contributions from all levels is highly appreciated.

.. hint::

  If you do not have an IHEP networking account, it is better to check out the
  official `Offline Software page
  <http://english.ihep.cas.cn/bes/doc/2247.html>`_ of BESIII. For this, you in
  turn need to be a BESIII member and have an SSO account, which can be done
  `here
  <http://afsapply.ihep.ac.cn/cchelp/en/accounts/#21-user-account-application>`__.

  BOSS can only be of use if you are a member of the BESIII collaboration and
  if you have access to the software of this collaboration. You can also have a
  look at the links in the section :doc:`appendices/z.references`.

Contents of the tutorial pages
------------------------------

This `GitBook <https://besiii.gitbook.io/boss>`_ provides tutorials for using
the BOSS Analysis Framework used in the BESIII collaboration. Currently, the
pages have been written from the perspective of (light) hadron spectroscopy,
but the tutorials can be useful for other forms of analysis as well.

Here are shortcuts that you might want to take:

#. :doc:`Getting started with BOSS <tutorials/getting-started>`.
   If you are not familiar with BOSS, it is best to start with this part of the
   tutorial. It will help you set up the BOSS environment in your account on
   the IHEP server ('install BOSS'), explain you some basics of the package
   structure on which BOSS is built, and guide you through the process of
   submitting jobs.

#. :doc:`Major BOSS packages </packages>`.
   Here, you will find descriptions of some of the important BOSS packages used
   in initial event selection, most notably, the :code:`RhopiAlg` package. This
   section is to serve as an inventory of BOSS packages.

#. :doc:`Physics at BESIII <physics>`.
   An inventory of important physics principles behind of data analysis at
   BESIII.

   *(These pages have not yet been written.)*

#. :doc:`Tips, Tricks, and Troubleshooting <appendices/tips/>`.
   These pages are used to collect problems that are frequently encountered
   when working with BOSS. As such, these notes are useful no matter your
   level. *New suggestions are most welcome!*


.. toctree::
  :maxdepth: 1

  bes3
  tutorials
  packages
  physics
  appendices
  contributing
