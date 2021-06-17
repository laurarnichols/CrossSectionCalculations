# Triply-hydrogenated Si vacancy (HSE/QE)

This folder currently contains the files needed to get the electronic matrix elements for a triply-hydrogenated
Si vacancy in a 216-atom (perfect-crystal) supercell at the HSE level using QE.

* Relaxation -- relax the perfect-crystal and defect-containing supercells at the PBE level using the Gamma point
* SCF (HSE) 
  * At the PBE level, an `nscf` calculation is used to calculate the eigenvalues on a denser k-point grid. 
  * `nscf` calculations cannot be performed using HSE functionals. 
  * Instead, do an `scf` calculation using the HSE functionals
* Export -- export both supercells
* TME -- input the exported results to calculate the electronic-transition matrix elements

