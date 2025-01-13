<!-- cspell:ignore Ctruth Xingyu Zhou zhouxy -->

# TopoAna

:::{note}

_Credit for the package goes to Zhou Xingyu_ <br> For more information, see the
[corresponding paper on arXiv](https://arxiv.org/abs/2001.04016).

:::

This package is an extremely helpful tool for analyzing the topologies of
{term}`Inclusive Monte Carlo simulation`. Inclusive MC samples give us valuable
information about the **background** of your analysis, as it allows you to know the true
contributions to that background. If you know what components that background exists of,
you can:

- try to make smart cuts to remove those background components;

- use a particular function that describes that background component best when applying
  a fit to the real data.

The problem with inclusive samples, however, is that they can include thousands of decay
modes. The `topoana` package allows you to make certain selections and to generate
tables that list frequencies of particles and decay modes that are of interest to you.

All versions of the package can be found here on
{ref}`the IHEP server <tutorials/getting-started/server:Accessing the server>`:

```text
/besfs5/users/zhouxy/tools/topoana
```

## Preparing initial event selection

The `topoana` package has to be run over a ROOT file that you have to prepare yourself.
The ROOT file has to contain a `TTree` with specific information of the Monte Carlo
truth:

- the **run ID** number

- the **event ID** number

- the **number of particles** in this event, which is necessary for loading the
  following arrays

- an array contain the **PDG code for each track** in this event

- an array containing the PDG code for the **mother of each track** (if available)

You can design a procedure to write this MC truth information yourself, but you can also
use either of the following two methods:

1. Add the `MctruthForTopo` algorithm package (see below) to the job options of your
   analysis.

2. Go through the code of the `MctruthForTopo` algorithm and take over the relevant
   components in your own initial event selection package, so that you can implement it
   within your cut procedure.

3. Use the `CreateMCtruthCollection` and `WriteMcTruthForTopoAna` in the `TrackSelector`
   base algorithm.

### The `MctruthForTopo` package

`MctruthForTopo` is an example package that comes with `topoana`. It can be used for
preparing a ROOT file sample that contains a `TTree` as described above. See the
documentation of `MctruthForTopo` for how these branches are typically called within
`MctruthForTopo-00-00-06`.

| Version    | Data type                                               |
| ---------- | ------------------------------------------------------- |
| `00-00-01` | No selection: all `McParticle` s are loaded             |
| `00-00-02` | Particles that don't come from a generator are rejected |
| `00-00-03` | Specifically designed for $J/\psi$                      |
| `00-00-04` | $J/\psi$, but with bug fix for `cluster` and `string`   |
| `00-00-05` | Designed for PID $90022$ and $80022$ (??)               |
| `00-00-06` | $4,180$ MeV data                                        |

See also
[decayFromGenerator](https://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#675a3679ea082c13d4ca4ce1c5571b59)

All versions of `MctruthForTopo` can be found here on the IHEP server:

```bash
/besfs5/users/zhouxy/workarea/workarea-6.6.5/Analysis/Physics/MctruthForTopoAnaAlg
```

You may choose a different version of BOSS than `6.6.5`, the one used above. If you have
sourced one of these versions (using `bash cmt/setup`), you can run it by adding the
following lines to your job options:

```text
ApplicationMgr.DLLs += {"MctruthForTopoAnaAlg"};
ApplicationMgr.TopAlg += {"MctruthForTopoAna"};
```

Note: Using `MctruthForTopoAna` is the quickest way to create a `TTree` containing the
necessary data for `topoana`, but it does not allow you to perform cuts: **all the
events** will be written to the `TTree` and no cut will be applied.

### Structure of the `Event::McParticleCol` collection

The `TTree` containing Monte Carlo data that is needed for `topoana` is created by
looping over the
[Event::McParticleCol](https://bes3.to.infn.it/Boss/7.0.2/html/namespaceEvent.html#b6a28637c54f890ed93d8fd13d5021ed)
in each event and writing the branches described above. To gain a better understanding
of what a package like `MctruthForTopo` does, let's have a look at the the contents of
the MC truth particle collection in one event:

<!-- markdownlint-disable -->

| Index | Particle |              |                   | Index | Mother |           |           |
| ----- | -------- | ------------ | ----------------- | ----- | ------ | --------- | --------- |
| `0`   | 23       | `Z0`         | $Z^0$             |       |        |           |           |
| `1`   | 22       | `gamma`      | $\gamma$          |       |        |           |           |
| `2`   | 4        | `c`          | $c$               | `0`   | 23     | `Z0`      | $Z^0$     |
| `3`   | -4       | `anti-c`     | $\bar{c}$         | `0`   | 23     | `Z0`      | $Z^0$     |
| `4`   | 91       | `cluster`    |                   | `3`   | -4     | `anti-c`  | $\bar{c}$ |
| `5`   | 443      | `J/psi`      | $J/\psi$          | `4`   |        | `cluster` |           |
| `6`   | 11       | `e-`         | $e^-$             |       |        |           |           |
| `7`   | 421      | `D0`         | $D^0$             | `5`   | 443    | `J/psi`   | $J/\psi$  |
| `8`   | 333      | `phi`        | $\phi$            | `5`   | 443    | `J/psi`   | $J/\psi$  |
| `9`   | -321     | `K-`         | $K^-$             | `7`   | 421    | `D0`      | $D^0$     |
| `10`  | 221      | `pi+`        | $\pi^+$           | `7`   | 421    | `D0`      | $D^0$     |
| `11`  | 321      | `K+`         | $K^+$             | `8`   | 333    | `phi`     | $\phi$    |
| `12`  | -321     | `K-`         | $K^-$             | `8`   | 333    | `phi`     | $\phi$    |
| `13`  | -13      | `mu+`        | $\mu^+$           | `11`  | 321    | `K+`      | $K^+$     |
| `14`  | 14       | `nu_mu`      | $\nu_\mu$         | `11`  | 321    | `K+`      | $K^+$     |
| `15`  | -11      | `e+`         | $e^+$             | `13`  | -13    | `mu+`     | $\mu^+$   |
| `16`  | 12       | `nu_e`       | $\nu_e$           | `13`  | -13    | `mu+`     | $\mu^+$   |
| `17`  | -14      | `anti-nu_mu` | $\bar{\nu}_{\mu}$ | `13`  | -13    | `mu+`     | $\mu^+$   |

<!-- markdownlint-enable -->

A few remarks about what we see here:

1. The structure of the decay chain is described by the index (see
   [Event::McParticle::trackIndex](https://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#34dae94b0ed5f36b875f783e61f8efc9)).
   Each particle is labeled by this index and if there is a mother particle, it is
   'linked' to its daughter by its index.

2. The decay chain starts with index `0`, a $Z^0$ boson that emerges right after the
   $e^+e^-$ collision, which then decays into a $c\bar{c}$ charm pair. In the
   simulation, this pair is taken to be a `cluster` (which has code `91`) or a `string`
   (which has code `92`).

3. For `TopoAna` (or actually any physics analysis), we are only interested in what
   happens after the formation of the cluster. This is where the meson is created to
   which the beam energy is tuned, in this case $J/\psi$. **We therefore only store
   particles that come after either particle code 91 or 92**, see
   `MctruthForTopoAna::execute`.

4. From the remainder of the table, we can see that the rest of the decay chain becomes
   (a rather rare if not impossible decay):

$$
J/\psi
\rightarrow D^0 \phi D^0
\rightarrow K^-\eta \phi
\rightarrow K^+K^-K^+
\rightarrow \mu^+\nu_\mu\mu^+
\rightarrow e^+\nu e\bar{\nu}\mu
$$

The main takeaway is that `topoana` requires you to store the branch with "track index"
{ref}`defined above <packages/analysis/topoana:Preparing initial event selection>` as
**having an offset**: the first particle is to be the initial meson (e.g. $J/\psi$) with
track index `0`, so that you can use the mother index as an array index. So you need to
subtract its original index from index of the the particles that come after. In
addition, the selection of MC truth particles is only to contain:

- Particles that result from the initial cluster or string, that is, everything that in
  this case comes after $J/\psi$.

- Only particles that come from the generator. This means they are not background
  simulated in the detectors and that that they were included in the decay chain from
  the generator. (See
  [Event::McParticle::decayFromGenerator](https://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#675a3679ea082c13d4ca4ce1c5571b59).)
  In this case, this means that everything that comes after the decay of $D^0$ and
  $\phi$ is to be excluded, because the $\mu^+$ and $K^+$ decays take place outside the
  BESIII detector.

- Only particles that have a mother particle (is not
  [primaryParticle](https://bes3.to.infn.it/Boss/7.0.2/html/classEvent_1_1McParticle.html#f225ad5eb24b49e277349c3ec2dd297e)).

In table format, with these conventions, the result that should be stored for the
`topoana` package would be:

<!-- markdownlint-disable -->

| Array index | Particle |         |          | Array index | Mother |           |          |
| ----------- | -------- | ------- | -------- | ----------- | ------ | --------- | -------- |
| `0`         | 443      | `J/psi` | $J/\psi$ | `-1`        | 91     | `cluster` |          |
| `2`         | 421      | `D0`    | $D^0$    | `0`         | 443    | `J/psi`   | $J/\psi$ |
| `3`         | 333      | `phi`   | $\phi$   | `0`         | 443    | `J/psi`   | $J/\psi$ |
| `4`         | -321     | `K-`    | $K^-$    | `2`         | 421    | `D0`      | $D^0$    |
| `5`         | 211      | `pi+`   | $\pi^+$  | `2`         | 421    | `D0`      | $D^0$    |
| `6`         | 321      | `K+`    | $K^+$    | `3`         | 333    | `phi`     | $\phi$   |
| `7`         | -321     | `K-`    | $K^-$    | `3`         | 333    | `phi`     | $\phi$   |

<!-- markdownlint-enable -->

## Installing topoana

Execute
[setup.sh](https://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/setup.sh)
and see the instructions there on how to source it. If you have done this, you can use
the command `topoana.exe` the output generated through the
{ref}`previous step <packages/analysis/topoana:Preparing initial event selection>`.

## Format of a topoana card

If you have
{ref}`prepared a ROOT file <packages/analysis/topoana:Preparing initial event selection>`
and {ref}`installed topoana.exe <packages/analysis/topoana:Installing topoana>`, you can
analyze the output. The `topoana` package will generate some tables containing
statistics of certain signal particles and signal decay modes. You can specify these
signal particles and branches through a `topoana` card and run the analysis with the
command `topoana.exe your_topoana.card`.

A `topoana` card file (`.card` extension) is a text file that defines the way in which
you execute `topoana.exe` on your data set. In this file, you for instance specify the
input ROOT files that you want to analyze.

The syntax of the `topoana` card is slightly reminiscent of `bash`. Starting a line
with:

- `#` means that the line is a comment and is therefore ignored;

- `%` means that the the line represents a field.

A opening curly brace (`{`) following a `%` sign means that a field block is opened. The
next line(s) contain the value(s) of that field. Close the block with a closing curly
brace (`}`).

The following pages list **all fields** that can be used in your `topoana` card:
{doc}`required </packages/analysis/topoana/required>` and
{doc}`optional fields </packages/analysis/topoana/optional>`.

## Tips on the results

_(From_ `topoana` _terminal output.)_

1. Statistics of the topologies are summarized in three types files: `pdf`, `tex` and
   `txt`. Although these are different formats, they contain the same information. The
   `pdf` file is the easiest to read. It has been converted from the `tex` file using
   the `pdflatex` command. If necessary, you can check the contents of the `txt` file as
   well (e.g. using text processing commands).

2. Tags of the topologies are inserted in all the entries of `TTree` for `topoana` in
   the output ROOT file(s). The ROOT files may have been split up, in which case you
   should load them using a `TChain`. Except for this, the `TTree` for `topoana` data of
   the output ROOT file is entirely the same as that of the input ROOT file(s). In
   addition, the topology tags are identical with those listed in the txt, tex, and pdf
   files.

## Submitting a `topoana.exe` job

Just like a BOSS job, you can submit a `topoana` job to the queue. This is useful if
your data is extensive and you want to log out while the job is executed. Just write
your command in a `bash` script like this:

```{code-block} bash
:caption: your_bash_file.sh
{ topoana.exe your_topoana.card; } &> your_file.log
```

The pipe (`>`) with the curly braces ensures that all output (including warnings) is
written to the log file (here, `your_file.log`).

Make sure that you make the `bash` script executable using `chmod +x your_bash_file.sh`.
You can then submit your job to the queue using:

```bash
hep_sub -g physics your_bash_file.sh
```

and keep an eye on your jobs using:

```bash
hep_q -u $USER
```

```{toctree}
:maxdepth: 1

topoana/required
topoana/optional
```
