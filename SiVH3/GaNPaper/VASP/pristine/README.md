# Pristine

* 2x2x2 supercell
* 5x5x5 Gamma-centered k-point mesh
* `ENCUT = 600` (based on Guanzhi's calculations)

## Tasks

- [x] Relax
- [x] SCF
- [ ] Export

## Notes

* With symmetry on, 2x2x2 supercell with 5x5x5 k-point mesh has 10 irreducible k-points
* With `ISYM = 0`, there are 63 irreducible k-points. I use `KPAR=7` on `14*44=616` processors.
