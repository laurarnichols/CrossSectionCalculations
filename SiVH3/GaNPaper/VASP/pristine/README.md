# Pristine

* 4x4x4 supercell
* Gamma-point k-point mesh
* `ENCUT = 400` (based on Guanzhi's calculations)
* Relaxation uses `EDIFF = 1E-5` and SCF uses tighter convergence of `EDIFF = 1E-8`
* `NBANDS` default for relax and 224 for SCF
* `ISYM` default for relax and 0 for SCF (to match defect calculation)
* Relax volume with `ISIF=3`

## Tasks

- [ ] Relax
- [ ] SCF
- [ ] Export (need to make output look spin-polarized to match defect calculation)

## Notes


