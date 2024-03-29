<!-- cspell:ignore randomtrg Xmanager -->

# The IHEP server (lxslc)

Within BESIII, most analysis tasks are run on a server that is hosted by {term}`IHEP`.
The server is also where you will use BOSS. You will need to
[apply for an IHEP computing account](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Lxslc_account_application)
to be able to log in.

## Accessing the server

The IHEP server runs on [Scientific Linux CERN](https://scientificlinux.org/) (SLC). The
server offers several versions. Usually, people use either SLC5, SLC6, or SLC7. The
domain names for these are `lxslc7.ihep.ac.cn`, where the `7` in this case refers to
SLC7. If you are running on Linux or a Linux terminal, the server can be easily accessed
using:

```bash
ssh -Y <your user name>@lxslc7.ihep.ac.cn
```

Here, the option `-Y` ensures _X11 forwarding_, allowing you to open graphical
applications from the server.

:::{note}

If you don't like having to enter your password every time you log in, have a look at
the section {ref}`appendices/tips:Key generation for SSH`.

:::

In Windows, there are some nice tools that allow you to access the server. First of all,
to be able to use SSH, use will either have to use [PuTTY](https://www.putty.org/) or
more extensive software like [Xmanager](https://www.netsarang.com/en/xmanager/). You can
also just search for some Linux terminals for Windows. In addition, have a look at the
(S)FTP client [WinSCP](https://winscp.net/eng/index.php). It allows you to easily
navigate the file structure of the IHEP server and to quickly transfer―even
synchronize―files up and down to your own computer.

:::{note}

Once in the server, you can switch to other versions of SLC using `hep_container`. So
for instance, if you are in SLC7 (CentOS) and want to use SL6, you can use:

```shell
hep_container shell SL6
```

where `shell` can be replaced with your shell of choice.

:::

## Important data paths

Some other important directories for the BESIII Collaboration are the following:

- [BOSS Software directory](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/How_to_setup_BOSS_environment_on_lxslc)

  - `/cvmfs/bes3.ihep.ac.cn/bes3sw/Boss` (also referred to with `$BesArea`)

- [Raw data files](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Raw_Data)

  - `/bes3fs/offline/data/raw`
  - `/besfs5/offline/data/randomtrg` (random trigger data)

- [Reconstructed data sets](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Production)

  - `/besfs3/offline/data/`
  - `/besfs/offline/data/` (older versions)

- [Reconstructed Monte Carlo sets](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Jpsi_data)
  (latest version available is `6.6.4`):

  - `/besfs2/offline/data/664-1/jpsi/09mc/dst` (2009; 225M)
  - `/besfs2/offline/data/664-1/jpsi/12mc/dst` (2012; 200M)
  - `/besfs2/offline/data/664-1/jpsi/12mc/grid/dst` (2012; 800M)
  - (no reconstructed MC samples available yet for 2018)

These directories will be important later in this 'tutorial'.

:::{note}

For the latest data file locations, see
[this page](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Production).

:::
