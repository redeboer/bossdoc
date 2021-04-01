# Generating exclusive Monte Carlo data

:::{todo}

Write contextual introduction.

:::

## Designing decay cards

When generating a Monte Carlo sample, a decay card (usual extension: `dec`) can
be used to overwrite the decay of certain particles. This allows you to
generate a Monte Carlo sample that only contains events with the signal
topology which you are studying.

A decay card is a text file that lists certain particle decays. If your decay
card specifies the decay channels of a certain particle, the 'normal' decay
channels (those listed in the PDG) for that particle will be overwritten. The
decay channels of one particle should follow this pattern:

```text
Decay <particle name>
  <branching fraction 1> <daughter 1a> <daughter 1b> <generator> <parameters>;
  <branching fraction 2> <daughter 2a> <daughter 2b ><generator> <parameters>;
Enddecay
```

Here, there are only two decay channels, but you can add more of course. Note
that a decay card **has to end with the line** :

```text
End
```

:::{warning}

Due to a small bug in BOSS, **a decay card has to end in with an empty white
line**, otherwise the simulation job will crash.

:::

If you do not specify the decay channels of a certain particle, the decay card
called `DECAY.dec` in the `BesEvtGen` package will be used. This file
essentially follows the PDG listings. In addition, definitions of particles
(including their physical widths) can be found in the file `pdt.table`. Both
files are located here (in the case of BOSS 7.0.4):

```text
/cvmfs/bes3.ihep.ac.cn/bes3sw/Boss/7.0.4/Generator/BesEvtGen/BesEvtGen-00-03-98/share
```
