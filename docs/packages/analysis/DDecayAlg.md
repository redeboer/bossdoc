<!-- cspell:ignore dtag -->

# DDecayAlg

{code}`DDecayAlg` is an algorithm used by BESIII to create {code}`NTuple` s to
be used in charm analysis (e.g. $D\to K_S^0 h^+h^-$.

It is located in {code}`BesExamples` of BOSS and mainly uses the
{code}`DTagTool` package to perform {code}`tagged` analysis of D mesons.

## DTagTool

The algorithm starts the {code}`DTagTool` algorithm

```text
DTagTool dtagTool;
```

{code}`DTagTool` has information about tagged decays at BESIII, used at the
$\psi(3770)\to D^0 \bar{D}^0$ decay mode. We can either look at the "single
tag" or "stag" which looks at the decay $D^0(\bar{D}^0) \to f$ where we include
both $D^0$ and $\bar{D}^0$.

Let's take the $K_{S}^{0} \pi^+ \pi^-$ decay, which {code}`DTagTool` assigns
the decay mode {code}`"100"` :

```text
EvtRecDTag * stag = dtagTool.findSTag(100);
```

This {code}`stag` object now has the information relating to the candidate
decay $D\to K *S^0 \pi^+ \pi^-$ such as $\Delta E = E* \text{beam} - E_D$:

```text
deltaE = stag->deltaE();
```

or the tracks from the event

```text
tracks = stag->tracks();
```
