# Triply-hydrogenated Si vacancy

This folder contains subdirectories that contain the needed files to calculate the electronic-transition matrix
elements in either QE or VASP using different functionals. Each calculation has a general form:

* Relax the initial (perfect-crystal) and final (captured-carrier, defect-containing) supercells at the Gamma point
* Perform a calculation for each supercell to get the energy bands on a denser k-point grid, given the relaxed geometry
* Export the results
* Calculate the matrix elements

## Relaxation

First, both the perfect-crystal and defect-containing supercells must be relaxed. This is done using a Gamma-point-only
calculation.

* The perfect-crystal supercell should be relaxed first with a variable-cell relaxation (`vc-relax`) to get the 
  ground-state cell size and atom positions.
* A defect should then be introduced into the relaxed perfect-crystal supercell and only the positions of the atoms 
  relaxed (`relax`) so that the cell size doesn't change and the two supercells remain comparable.
* The relaxed geometry from each of these calculations should be copied from the `.out` file into the `.in` files of 
  the following `nscf` calculations.

## NSCF or SCF (HSE)

An `nscf` calculation calculates the eigenvalues for a well-defined k-point grid based on input from a previous `scf`
(or relaxation) calculation. This calculation is the next step for both the perfect and the defect-containing crystals
at the PBE level in order to find the eigenvalues for a denser k-point grid than is used for the relaxation. 

`nscf` calculations cannot be done with HSE functionals, so an `scf` calculation must be performed instead to find the 
eigenvalues at the denser k-point grid.

* The original paper was based on a 3x3x3 k-point grid with symmetry turned off (`nosym = .TRUE.`). 
* Turning the symmetry off is important to ensure that the `TME` calculation gets all of the k-points.
* Make sure that you have copied the optimized geometry from the previous relaxation calculation.

## Export

Both of the results must be exported to files usable by the `TME` code using the proper version of the QE- or VASP-based Export program.

## TME

The matrix elements can finally be calculated from the exported results. 

* `iBandFinit` and `iBandFfinal` are usually currently set to the same value: the band index of the final electronic state within
  the defect-containing crystal.
* `iBandIinit` and `iBandIfinal` represent the range of conduction states to calculate the matrix element from, with `iBandIinit` 
  typically being the bottom of the conduction band in the perfect-crystal supercell and `iBandIfinal` being the highest band in 
  the perfect-crystal supercell that you want to consider.
