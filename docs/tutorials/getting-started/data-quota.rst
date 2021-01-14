Data quota
==========

When you have logged into the server, you usually start in your home
(:code:`~`) folder. Move to the root of the server (:code:`cd /`) and you'll
see that is a large number of other directories. A few of these directories
contain space that is assigned to your user account. Here is an overview:

.. list-table::
  :header-rows: 1

  * - Path
    - Data quota
    - Max. number of files
    - Remark
  * - :code:`/afs/ihep.ac.cn/users/<letter>/$USER`
    - 500 MB
    - NA
    - home (:code:`~`)
  * - :code:`/besfs5/users/$USER`
    - 50 GB
    - 300,000
    -
  * - :code:`/ihepbatch/bes/$USER`
    - 200 MB
    - NA
    -
  * - :code:`/workfs/bes/$USER`
    - 5 GB
    - 50,000
    - no :code:`hep_sub` available
  * - :code:`/scratchfs/bes/$USER`
    - (500 GB)
    - NA
    - max. 2 weeks*


* In practice, files remain on this server indefinitely. In fact,
  :code:`scratchfs` seems to follow a less strict policy then other folders.

.. warning::
  **Do not exceed these quotas!** If you do, the folder of which you are
  exceeding its quota will be locked by the Computing Center after a few weeks
  and it is quite a hassle to regain access.

Official information on the quota can be found `here
<http://afsapply.ihep.ac.cn/cchelp/en/experiments/BES/#712-storage>`_.
