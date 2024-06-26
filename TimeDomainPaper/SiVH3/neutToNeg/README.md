# Neutral-to-negative transition

This file contains all of the choices made for the neutral-to-negative transition.

The ground state of the triply-hydrogenated Si vacancy is neutral. In order to have an additional electron captured into the defect, we must have that electron come from somewhere. You could have a donor in the supercell, but that would cause convergence and accuracy issues. Instead, you could insert a hole in the valence band as a "donor" and have the "additiona carrier" start in the conduction band, then transition to the defect. This strategy is used in the final state with two electrons in the defect and a hole in the valence band. However, the practical difference of placing the carrier in the conduction band vs the valence band for the initial state is minimal, so the initial state is just treated as the ground-state system with a neutral defect. 

Because of this choice, the total energies must be adjusted to reflect that the initial state energy should be higher by the band-gap energy. This correction is included in the `EnergyTabulator` calculations through `eCorrectTot = -1.194` eV (based on [the way the energy correction is included in the total energy difference](https://github.com/laurarnichols/defectCrossSections/tree/master/EnergyTabulator). In `EnergyTabulator`, the reference band can either be set to the VBM (where the reference carrier is) with `eCorrectEigRef = -1.194` eV or set to the CBM with no energy correction. I chose the latter in my calculations. I am doing gamma-point only for this transition to compare with Guanzhi, so I was able to use the HSE eigenvalues, which means that the energy difference between the VBM and the defect level are presumed to be accurate with no correction needed. Ran this on 128 processors (1 node), and it took 8 seconds.

The transition matrix element code does not include any meaningful choices. You must simply specify the band bounds for the initial state and the final state. The defect is at band 1024 in our system, and we want to consider about a 1 eV range for our plots, so we use 1025-1088 as the initial-state range. I used 256 processors, and it took 6 minutes.

For the LSF code, the second spin channel should be selected because that is where the carrier is transitioning. We used the following parameters:
```f90
 temperature          = 300
 dt                   = 2.1d-9
 hbarGamma            = 1.0    ! meV
 smearingExpTolerance = 1d-4
```
The same initial and final bands were used as in the TME code. I ran this on 256 processors, and it took 6 minutes.
