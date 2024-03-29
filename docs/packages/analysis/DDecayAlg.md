<!-- cspell:ignore dtag -->

# DDecayAlg

`DDecayAlg` is an algorithm used by BESIII to create `NTuple` s to be used in charm
analysis (e.g. $D\to K_S^0 h^+h^-$.

It is located in `BesExamples` of BOSS and mainly uses the `DTagTool` package to perform
`tagged` analysis of D mesons.

## DTagTool

The algorithm starts the `DTagTool` algorithm

```text
DTagTool dtagTool;
```

`DTagTool` has information about tagged decays at BESIII, used at the
$\psi(3770)\to D^0 \bar{D}^0$ decay mode. We can either look at the "single tag" or
"stag" which looks at the decay $D^0(\bar{D}^0) \to f$ where we include both $D^0$ and
$\bar{D}^0$.

Let's take the $K_{S}^{0} \pi^+ \pi^-$ decay, which `DTagTool` assigns the decay mode
`"100"`:

```text
EvtRecDTag * stag = dtagTool.findSTag(100);
```

This `stag` object now has the information relating to the candidate decay
$D\to K *S^0 \pi^+ \pi^-$ such as $\Delta E = E* \text{beam} - E_D$:

```text
deltaE = stag->deltaE();
```

or the tracks from the event

```text
tracks = stag->tracks();
```
