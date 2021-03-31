<!-- cspell:ignore guestpass offlinedb -->

# Data sets

This section explains the different data sets that can be processed using BOSS.
There are essentially three types of data files of relevance here:

- **Raw data** <br> These are data files containing raw recorded data from
  either real measurements in BESIII or from Monte Carlo simulations.
  Extension: `rtraw` or `raw`, see
  [here](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/How_to_mix_two_MC_samples)
  for how to convert them into each other.

- **Reconstructed data** <br> Raw files are too large to be handled in an
  analysis: the recorded data first has to be converted to tracks data. The
  output of this reconstruction step is a DST file. Extension: `dst`.

- **Output from the initial event selection** <br> In the analysis step, you
  analyze the events contained in the DST files. The output of that analysis is
  stored to a `TTree` in a ROOT file. Extension: `root`

## Locations on the IHEP Server

Inventories of the latest file locations are found on the Offline Software
pages (requires login):

- [Raw data](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Raw_Data)
- [Reconstructed data](https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Production)

In general, all data files are located on the BESIII file system (`besfs5`)
folders on the {doc}`IHEP Server </tutorials/getting-started/server>`. There
are a few different folders, because the files have been distributed to
different servers.

- `besfs5`: contains user files only

- `besfs2`: a symbolic link that points to `/besfs3/offline/data/besfs2`.
  Contains inclusive Monte Carlo samples.

- `besfs3`: file system that contains files of the runs before 2018

- `bes3fs`: a newer file system that contains for instance 2018 data

Within these folders, the data files are located under `offline/data` (e.g.
`/besfs3/offline/data`) and then the BOSS version with which these files have
been created.

```{warning}
Make sure you do not confuse the numbers when navigating these paths.
```

## Querying for data sets

### On `lxslc`

You can find all information about the data sets through MySQL on `lxslc`. To
open the database, type:

```text
mysql --user=guest --password=guestpass -h bes3db2.ihep.ac.cn offlinedb
```

Now it's a matter of searching through the database through MySQL query
commands. Some examples (in this case to find the exact energies of the data
set):

- `show tables;`
- `select * from MeasuredEcms where sample = "4360";`
- `select * from MeasuredEcms2 limit 20;`

For a reference of MySQL queries, see
[here](https://dev.mysql.com/doc/refman/8.0/en/).

Note that there are a few BOSS packages that allow you to fetch data from the
MySQL database from the C++ code. The main one is
[DatabaseSvc](http://code.ihep.ac.cn/bes3/BOSS/tree/master/workarea/Database/DatabaseSvc).
For fetching exact beam energy values, use
[MeasuredEcmsSvc](http://code.ihep.ac.cn/bes3/BOSS/tree/master/workarea/Utilities/MeasuredEcmsSvc).

### Web interface

Alternatively, you can have a look at this page
<br>[http://bes3db.ihep.ac.cn/online/webserver/runinfo/runparams.php](http://bes3db.ihep.ac.cn/online/webserver/runinfo/runparams.php)
<br>for an overview of run numbers et cetera.

```{toctree}
:maxdepth: 1

data/measurements
data/inclusive
data/exclusive
```
