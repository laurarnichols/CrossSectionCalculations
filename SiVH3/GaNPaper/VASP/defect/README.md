# Triply-hydrogenated Si vacancy

* 2x2x2 supercell
* 5x5x5 Gamma-centered k-point mesh
* `ENCUT = 600` (based on Guanzhi's calculations)
* Relaxation uses `EDIFF = 1E-5` and SCF uses tighter convergence of `EDIFF = 1E-8`
* Use same volume as pristine cell and relax only internal DOF with `ISIF=2`

## Tasks

- [x] [Relax defect in ground state (neutral) then SCF](./finalChargeState/finalPositions)
- [x] [Excite carrier out of defect into band and re-relax then SCF](./initialChargeState)
- [x] [SCF for ground state in excited-state positions](./finalChargeState/initialPositions)
- [ ] Export

## Notes

* Even without messing with the symmetry tag, there are 63 irreducible k-points (same as in perfect crystal with `ISYM=0`