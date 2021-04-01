# Data quota

When you have logged into the server, you usually start in your home (`~`)
folder. Move to the root of the server (`cd /`) and you'll see that is a large
number of other directories. A few of these directories contain space that is
assigned to your user account. Here is an overview:

<!-- markdownlint-disable -->

| Path                                   | Data quota | Max. number of files | Remark                 |
| -------------------------------------- | ---------- | -------------------- | ---------------------- |
| `/afs/ihep.ac.cn/users/<letter>/$USER` | 500 MB     | NA                   | home (`~`)             |
| `/besfs5/users/$USER`                  | 50 GB      | 300,000              |                        |
| `/ihepbatch/bes/$USER`                 | 200 MB     | NA                   |                        |
| `/workfs/bes/$USER`                    | 5 GB       | 50,000               | no `hep_sub` available |
| `/scratchfs/bes/$USER`                 | (500 GB)   | NA                   | max. 2 weeks           |

<!-- markdownlint-enable -->

::::{margin}

:::{note}

As of February 22nd, 2021, the old file system `besfs` has been superseded by
`besfs5` for both users and groups.

:::

::::

In practice, files remain on this server indefinitely. In fact, `scratchfs`
seems to follow a less strict policy then other folders.

:::{warning}

**Do not exceed these quotas!** If you do, the folder of which you are
exceeding its quota will be locked by the Computing Center after a few weeks
and it is quite a hassle to regain access.

:::

Official information on the quota can be found
[here](http://afsapply.ihep.ac.cn/cchelp/en/experiments/BES/#712-storage).
