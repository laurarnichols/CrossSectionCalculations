# VASP calculations and Export

We need the following main things from the VASP calculations:
* Perfect-crystal wave functions for zeroth-order matrix elements
* Final charge state/initial positions wave functions for both-order matrix elements
* HSE-level total energies for delta function and zeroth-order matrix elements
* Eigenvalues for delta function, matrix elements, and plotting (can be HSE or PBE; ground state is more accurate)
* Initial and final relaxed geometries to get shift in positions after capture

## Tasks

- [ ] [Perfect crystal](./pristine)
- [ ] [Final charge state/final positions](./finalChargeState/finalPositions)
- [ ] [Initial charge state](./initialChargeState)
- [ ] [Final charge state/initial positions](./finalChargeState/initialPositions)

## Calculation choices

Ideally, we would like to use HSE-level calculations and converge the cross section with respect to the supercell size and the k-point grid. However, VASP calculations must be done for every phonon mode individually for the frist-order matrix elements. The number of modes and length of the VASP calculations increases rapidly with superell size, so we are limited in our choices. 

Here are the choices we have used for supercell and k-point grid:

* 2x2x2 supercell with a 5x5x5 k-point grid
  * Made HSE calculations more feasible
  * Sok argued that that supercell is just way too small for defect calculations
* 4x4x4 supercell at gamma for matrix elements and 2x2x2 supercell with a 3x3x3 k-point mesh for the phonons
  * Matrix elements more converged
  * Fewer phonon modes meant fewer first-order calculations
  * Limited by slow speed of current version of `Export` and `TME`
  * May or may not be okay to use smaller set of phonon modes and would be difficult to repeat
  * I parallelized and optimed `TME` and `Export` so that we could use bigger supercells and all of the phonon modes
* 4x4x4 supercell at gamma for all calculations
  * Finally got to cross section results, but there were huge gaps in the energy levels
  * Sok and Xiaoguang said that this was due to there no being enough k-points
* 4x4x4 supercell at gamma for first-order (?) and 3x3x3 grid for zeroth-order
  * Xiaoguang suggested that we do a 3x3x3 grid and calculate the cross section for each k-point independently, then smear the final results to combine
  * Seems feasible for the zeroth-order, but I think it may take too long for the first-order
  * Doing zeroth-order first, then going to estimate how long the first-order will take and try to think if there's a way to make it work for the first-order


Guanzhi considered the 0/- transition. He originally considered the ground-state (neutral) defect in the relaxed positions of the neutral defect for all of the matrix elements (initial charge state/initial positions). Technically, because he considers the 0/- transition, his final state for the matrix element should be the negatively-charged defect in the neutral-defect-relaxed positions (final charge state/initial postions); however, Xiaoguang and Sok said that the wave functions probably would not change for the two charge states and that the choice is justified given that the excited-state calculations are so much more difficult to converge (they really aren't for Si, but may be in the future). He later came back and said something about using the final charge state, so he may have switched, but I am not sure.

Guanzhi also treated the perfect crystal as spin-polarized (`ISPIN=2`) even though that's not needed because he said it made it easier to match the output up with the defect results. I used `ISPIN=1` for the perfect crystal because I updated the `Export` and `TME` codes to consider spin-polarization properly. He also used `ISYM=-1` to avoid mistakes, but the Export code seems to handle the weight of the k-points with `ISYM=0`, so that is what I planned to use. However, when I mentioned having 14 k-points to Xiaoguang, he said that we should use the full 27-point k-mesh to get the most energies. I am not sure if including the $\mathbf{k}/-\mathbf{k}$ pairs will add to the available energy levels, so I went ahead and included all of the k-points with `ISYM=-1`; however, this is something to look at to see if using `ISYM=0` would be usable in the future because it would be much faster. Using `ISYM=0` could also make the first-order matrix elements more feasible.

### Input parameters

Full input files are given in individual folders, but the main parameter choices and changes between calculations are given below.

* Relaxation:
```
ENCUT  = 400      ! cutoff energy
EDIFF  = 1E-5     ! convergence threshold
EDIFFG = -1E-2    ! Convergence for ionic relaxation
```
* SCF
```
NBANDS = 1540      ! Number of bands
ENCUT  = 400      ! cutoff energy
EDIFF  = 1E-8     ! convergence threshold
ISYM = -1         ! Turn symmetry completely off
```
* NSCF (same as SCF, but use `ICHARG=11`)
* I used `NCORE=11` for PBE and `NCORE=4` for HSE because there are 44 cores per node on the machine I worked on
* HSE
```
LHFCALC  = .TRUE. ! Turns on doing the hybrid functional
HFSCREEN = 0.2    ! Screening length, we won't adjust this
AEXX     = 0.23   ! This is the amount of exact exchanged mixed in, we'll need to check
```

## Notes

* Relax unit cell first to get lattice parameter, then fix lattice parameters in further calculations
* Relax perfect crystal supercell first, then use that as starting point to introduce defect 
* For the defect, used the following order of calculations to speed things up:
  * Ground state relax (final charge state/final positions)
  * Use outputs to start excited-state relax (initial charge state)
  * Use outputs to start ground-state SCF at excited state positions (final charge state/initial positions)
* VASP requires that an SCF calculation follow a relaxation to match the charge density and wave functions to the final positions
* The `Export` program also assumes that the calculation does not include relaxation steps with multiple energies
* For an individual system, do relax first, then SCF with tighter convergence, then NSCF for denser grid (if needed)
* Guanzhi said that he determined that `ENCUT = 400` eV was sufficient for this system, so that is what I will use.
* For relaxations, I use `EDIFF = 1E-5` for speed, then I tighten to `1E-8` for the SCF calculations for better-converged wave functions (see [this forum post by Andy](https://www.vasp.at/forum/viewtopic.php?f=3&t=18050))
* I use non-spin-polarized calculations for the perfect crystal and spin-polarized for the defect crystal.
* We need symmetry turned off (`ISYM=0`) for feeding into the Export code, but for relaxations I leave the symmetry alone for speed.
* Used `vasp_gam` (gamma-only) version of VASP to speed up HSE calculations. `Export` currently doesn't work properly for gamma-only, but I cut everything out besides the energy stuff because that is all we need.
* The HSE calculations are faster when using results from a PBE calculation, but you can't use the results from the `vasp_std` version as input to the `vasp_gam` version because it will say `plane wave coefficients changed`. Instead, do a PBE calculation using `vasp_gam` to use as input for the HSE calculations.
* __Important__: Our code has not been compiled properly on Perlmutter yet. I am in the process of trying to distribute the arrays better to get rid of the seg faults. Those are gone, but the results are not correct, so the code still needs some debugging.

