# Triply-hydrogenated Si vacancy

* 4x4x4 supercell
* Gamma-point k-point mesh
* `ENCUT = 400` (based on Guanzhi's calculations)
* Relaxation uses `EDIFF = 1E-5` and SCF uses tighter convergence of `EDIFF = 1E-8`
* Use same volume as pristine cell and relax only internal DOF with `ISIF=2`

## Tasks

- [ ] [Relax defect in ground state (neutral)](./finalChargeState/finalPositions) (running)
- [ ] [Excite carrier out of defect into band and re-relax](./initialChargeState)
- [ ] [SCF for ground state in excited-state positions](./finalChargeState/initialPositions)
- [ ] Export

## Notes

