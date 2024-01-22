# VASP Flags and Calculations

## Relaxation

* Start a new calculation from scratch: `ISTART=0`, `ICHARG=2`, `INIWAV=1`
* Turn on relaxation: `IBRION=2`
* Determine what to relax: `ISIF=2` for atoms, `ISIF=3` for atoms and cell
  * _Note:_ You can also specify what lattice coordinates you want to allow to relax by manually setting the forces in the other directions to 0. 
  * To do this, edit the `src/constr_cell_relax.F` file.
  * Follow the directions in the file to save the force(s) you want to keep and zero out the others.
  * Save your original executable in a different-named file and recompile.
  * You can then change the name of the new executable (e.g., `vasp_std_constr_relax_c_only`) and move the original back to the original name.
* Set the number of relaxation steps: `NSW=300` is a typical value
  * Don't have to use a huge wall clock and `NSW`
  * Can split into shorter runs
  * If it runs more than one step and doesn't say it reached relaxation, then you can continue the calculation as follows
    * `cp POSCAR POSCAR.n`, where `n` is the calculation number (you don't have to save all of these, but at least saving the original is important)
    * `cp CONTCAR POSCAR`
    * Save standard out to keep tabs (e.g., `cp GaN_relax.out GaN_relax.out.01`)
    * Set `ISTART/ICHARG = 1/1` if it isn't already
    * Rerun the job
* Write out the wave function and charge density for subsequent scf calculation: `LWAVE=.TRUE.`, `LCHARG=.TRUE.`

## SCF

* Always do an scf calculation after a relaxation to calculate the charge density from the final atomic positions
* VASP does electronic portion then moves the atoms, so you need to manually do the electronic portion after relaxation
* Copy `CONTCAR` to `POSCAR` to get the final positions from the relaxation
* Use `ISTART=1` and `ICHARG=1` to read in the final wave function and charge density
* Remove `INIWAV` as it is meaningless when reading in the wave function
* Turn off relaxation with `IBRION=-1` and `NSW=0`
* Remove `ISIF` and `EDIFFG` as they are meaningless when not doing relaxation

### NSCF

* This calculation can be used to get band energies at denser k-point grids using the relax/scf calculation as a starting point
* For HSE, cannot do an NSCF calculation because of how the exact exchange is calculated
* Everything is the same as SCF, except `ICHARG=11`

## HSE

You can do relaxations or SCF calculations at the HSE level for better accuracy. The mixing parameter should be tuned to match the experimental band gap. For detailed notes on hybrid-functional theory and calculations see the [hybrid theory and calculations](hybridTheoryAndCalculations.md) note.


## Band-decomposed charge densities

In VASP, use:
```fortran
LPARD = .TRUE.
LSEPB = .TRUE.
IBAND = N1 N2 ...
```
where the `N`'s are the band indices you want to look at. *Note: the wave function must already be converged from a previous calculation.*

Andy created a script to fix formatting issues that sometimes arise and split the charge density into spin channels. Both python scripts can be found in the [`Tools` folder of the `defectCrossSections`](https://github.com/laurarnichols/defectCrossSections/tree/a16a86926f5b1d08ee571c8cd404b545f3a428ac/Tools) repo that holds our main code. 