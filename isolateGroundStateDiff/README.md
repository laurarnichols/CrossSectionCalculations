# Isolate Ground State Difference

Guanzhi did two calculations at the ground state (HSE level) with the intent to compare different choices for `ISMEAR` and got different results. However, 
his calculations not only included a change in `ISMEAR` (`ISMEAR=0`/`SIGMA=0.03` vs `ISMEAR=-2`), but they also included a change in `LDIAG` (`.TRUE.` vs 
`.FALSE.`). Xiaoguang also said that the difference could be an issue with the k-point grid not being converged, although Andy said Gamma should be
fine for our supercell size. 

To figure out what the difference is, I am going to compare the `ISMEAR` choices at the PBE level in the ground state on top of the PBE-relaxed, 
excited-state structure. If those are the same, I will then reproduce Guanzhi's HSE calculations and compare different choices of `LDIAG`. If the different 
`ISMEAR` choices aren't the same at the PBE level, I will increase the k-point grid density until I can get the results to match.

Based on the input file that Guanzhi sent (`INCAR_Guanzhi`), he was doing an SCF calculation at the HSE level on top of the PBE-optimized geometry. I will
use `ISMEAR=0` to compare the effect of `LDIAG` at the HSE level.

## Tasks

- [x] PBE
  - [x] `ISMEAR=-2`
  - [x] `ISMEAR=0`, `SIGMA=0.03`
- [x] HSE
  - [x] `LDIAG=.TRUE.`
  - [x] `LDIAG=.FALSE.`

## Results

Did not see any difference with `ISMEAR` or `LDIAG` choice at either level. Guanzhi came back and said that the difference he saw was in going from either
`ISMEAR=-2`/PBE or `ISMEAR=0`/HSE to WZP VBM HSE. Andy said that he didn't trust the `LDIAG` tag and we should avoid it if possible. 
