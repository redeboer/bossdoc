<!-- cspell:ignore Etrs -->

<!--
The following fields do not have to be specified, but are useful for larger
-->

# Optional fields

```{todo}
Many of the below fields still have to be tested and described.
```

## Maximum fields

### Maximum number of entries to be processed

Speaks for itself:) Do not use scientific notations like `1e5` for $10^5$, but
use `10000`.

### Maximum hierarchy of heading decay branches to be processed in each event

### Maximum number of decay trees to be printed

### Maximum number of decay final states to be printed

### Maximum number of entries to be saved in a single output root file

### Maximum number of decay trees to be analyzed

## `Cuts`

### Cut to select entries

This field only supports one line. The syntax should be the same as when you
apply a cut selection for in the
[TTree::Draw](https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45)
method.

### Method to apply cut to array variables (Two options: T and F. Default: F)

Whether or not to apply the cut to the array variables as well. Set to true
(`T`) if you want to apply the cut there as well.

## Ignore fields

### Suppress the first branches of decay trees in the output txt/tex/pdf files

Initial decays (e.g. $e^+e^- \rightarrow J/\psi$) are not listed in the tables.

### Suppress the topology tags in the output tex/pdf files

The following columns are not written:

- **Decay trees and their respective final states**: iDcyTr and iDcyFSt

- **Table Signal particles**: iSigP

- **Signal decay final states**: iSigDcyFSt2 and iDcyFSt

### Ignore gISR photons (Two options: Y and N. Default: Y)

### Ignore gFSR photons (Two options: Y and N. Default: Y)

### Ignore the decay of the following particles

This field allows you to filter away certain **mother** particles. The decays
will _not be listed in any table_.

### Ignore the decay of the daughters of the following particles

This field allows you to filter away certain **daughter** particles. The decays
will _not be listed in any table_.

## What to perform

### Process charge conjugate objects together (Two options: Y and N. Default: N)

Adds two additional columns: nCcEtrs and nTotEtrs, where conjugate particles
are counted together.

Skip the topology analysis of decay trees and decay final states (Two options:

### Y and N. Default: N)

Set this field to `Y` if you do not want to generate the tables that list _all_
decay topologies. **It is important to set this field if you are dealing with
large data** and are only interested in certain inclusive decays! In this case,
you should also make use of the signal fields.

Perform the topology analysis of the decay branches begun with the following

### particles

For each particle you list here, a table of decays where this particle was the
mother particle. No table is created if the particle does not decay in any of
the events. You can limit the number of rows by adding a number on the same
line, separated with some white-spaces. The remainder will then be collected
into a final "rest" row of $\text{particle} \rightarrow \text{others}$.

Perform the topology analysis of the exclusive decay branches matched with the

### following inclusive decay branches

This field allows you to generate separate tables of decays involving a certain
process. The lines should be numbered. The first line represents the initial
state in a certain process, the following lines list the decay products you
want to limit yourself to. The string $+ \text{anything}$ will be added
automatically (see terminal output). See
[here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta3_extensions/ta32/ta322/ccbar_topoana.card)
for an example of syntax.

## Signal fields

### Signal particles

If this field is filled, an additional table is generated with **counts of the
signal particles** you specified. List the particles using line breaks (do not
use commas).

### Signal inclusive decay branches

Here you can list the final state(s) of the signal decay(s) that you are
looking for. Naturally, the order of the decay particles does not matter. The
syntax is as follows:

- Start a line with a number (starting with `0`), then in the same line add a
  space or tab, and name list the decay particle according to the PDG plain
  name (e.g. $pi+$ for $\pi^+$).

- Continue the next line of the same state description with a `1` and so forth.

- You can name several inclusive decay states by starting each series with a
  `0` again.

- See an example for the syntax
  [here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta4_signals/ta42_sig_inc_evt_brs/ta423/uubar_topoana.card).

### Signal sequential decay branches

See
[here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta4_signals/ta43_sig_seq_evt_brs/ta431_3_2/mixed_topoana.card)
for an example of syntax.

### Signal inclusive sequential decay branches

See an example of syntax
[here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta4_signals/ta44_sig_inc_seq_evt_brs/ta441/Dz2KsPiPi_topoana.card).

### Signal intermediate-resonance-allowed decay branches

See
[here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta4_signals/ta45_sig_ira_evt_brs/ta451/mixed_topoana.card)
for an example of syntax.

### Signal inclusive or intermediate-resonance-allowed sequential decay branches

See
[here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta4_signals/ta46_sig_inc_or_ira_seq_evt_brs/ta463_2/mixed_topoana.card)
for an example of syntax. The asterisk (`*`) can be used as a short version of
the word "anything" in order to simplify your input.

### Signal decay trees

See
[here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta4_signals/ta47_sig_evt_trs/ta462/mixed_topoana.card)
for an example of syntax.

### Signal decay final states

See
[here](http://code.ihep.ac.cn/redeboer/IniSelect/-/tree/master/workarea/Analysis/TopoAna/v1.6.9/tutorials/ta4_signals/ta48_sig_evt_f_sts/ta472/mixed_topoana.card)
for an example of syntax.
