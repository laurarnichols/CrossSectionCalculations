# VASP calculations

* All calculations here are done on 2x2x2 supercells with a 5x5x5 Gamma-centered k-point mesh. 
* Guanzhi said that he determined that `ENCUT = 600` eV was sufficient for this system, so that is what I will use.
* For relaxations, I use `EDIFF = 1E-5` for speed, then I tighten to `1E-8` for the SCF calculations for better-converged wave functions (see [this forum post by Andy](https://www.vasp.at/forum/viewtopic.php?f=3&t=18050))
* I use non-spin-polarized calculations for the perfect crystal and spin-polarized for the defect crystal.
* We need symmetry turned off (`ISYM=0`) for feeding into the Export code, but for relaxations I leave the symmetry alone for speed.
