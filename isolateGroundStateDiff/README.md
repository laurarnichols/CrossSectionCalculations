# Isolate Ground State Difference

Guanzhi did two calculations at the ground state (HSE level) with the intent to compare different choices for `ISMEAR` and got different results. However, 
his calculations not only included a change in `ISMEAR` (`ISMEAR=0`/`SIGMA=0.03` vs `ISMEAR=-2`), but they also included a change in `LDIAG` (`.TRUE.` vs 
`.FALSE.`). Xiaoguang also said that the difference could be an issue with the k-point grid not being converged, although Andy said Gamma should be
fine for our supercell size. 

To figure out what the difference is, I am going to compare the `ISMEAR` choices at the PBE level in the ground state. If those are the same, I will then 
reproduce Guanzhi's HSE calculations and compare different choices of `LDIAG`. If the different `ISMEAR` choices aren't the same at the PBE level, I will
increase the k-point grid density until I can get the results to match.

## Tasks

- [x] PBE
  - [x] `ISMEAR=-2`
    - [x] Relax
    - [x] SCF (started)
  - [x] `ISMEAR=0`, `SIGMA=0.03`
    - [x] Relax 
    - [x] SCF (started)

## Notes on Results

* No difference in total energies between different `ISMEAR` settings at PBE level
