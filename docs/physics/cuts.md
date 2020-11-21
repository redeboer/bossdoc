# Cutting

## Typical cuts

In papers from the BESIII Collaboration, you will usually encounter the
following cuts. They are also listed
`here <https://docbes3.ihep.ac.cn/~offlinesoftware/index.php/Recommend_cuts>`\_
(requires login).

### Charged tracks

- Distance of closest approach of the track to the interaction (IP) in $xy$
  plane: $\left|\text{d}r\right| < 1\text{ cm}$.

- Distance of closest approach of the track to the IP in $z$ direction:
  $\left|\text{d}z\right| < 10\text{ cm}$.

- Polar angle: $\left|\cos\theta\right| < 0.93$.

- PID: usually making use of
  {ref}`MDC <physics/besiii:Muon Chamber System (MUC)>` and
  {ref}`TOF <physics/besiii:Time-Of-Flight System (TOF)>` and using a
  probability of at least $0.001$.

Sometimes: events with non-zero net charge are rejected.

### Neutral tracks

Neutral tracks are reconstructed from electromagnetic showers in the
{ref}`EMC <physics/besiii:Electromagnetic Calorimeter (EMC)>`, which consists
of a barrel and an end cap.

```{list-table}
---
header-rows: 1
---
* - Energy for **barrel** showers
  - $\cos\theta < 0.8$
  - $E > 25\text{ MeV}$
* - Energy for **end cap** showers
  - $0.86 < \cos\theta < 0.93$
  - $E > 50\text{ MeV}$
```

If there is more than one charged track, there is a time requirement of
$0 \leq T \leq 14$ ($50\text{ ns}$).

### Kinematic fits

- $\chi^2$ of the kinematic fit is often determined in the final event
  selection with a efficiency scan using a Figure-Of-Merit. To limit the amount
  of events stored, a cut-off value of $\chi^2 < 200$ is usually used.

## Cut flow

Cut flow is usually represented in the form of a table that lists the cuts and
the corresponding number of events that passed the cut. This gives you insight
in how much signal remains after your cuts, but also gives some idea of
efficiencies if you make a cut flow table for an exclusive Monte Carlo sample.

A typical example would be (with some thought up numbers):

```{list-table}
---
header-rows: 1
---
- - Total number of events
  - $100,000$
  - $100\%$
- - Number of events with $m$ number of charged tracks
  - $53,234$
  - $53\%$
- - Number of events with _at least_ $n$ neutral tracks
  - $43,156$
  - $43\%$
- - Number of events with exactly the final state particles
  - $20,543$
  - $21\%$
- - Number of events with $\chi^2$ for the kinematic fit
  - $18,163$
  - $18\%$
- - Number of events that passed reconstructed mass cut
  - $15,045$
  - $15\%$
```
