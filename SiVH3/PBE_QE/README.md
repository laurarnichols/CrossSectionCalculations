# Triply-hydrogenated Si vacancy (PBE/QE)

This folder currently contains the files needed to get the electronic matrix elements for a triply-hydrogenated
Si vacancy in a 216-atom (perfect-crystal) supercell at the PBE level using QE.

*Note: The results in the paper are based on PBE/QE calculations*

* Relaxation -- relax the perfect-crystal and defect-containing supercells using the Gamma point
* NSCF -- perform an `nscf` calculation to get the eigenvalues on a denser k-point grid
* Export -- export both supercells
* TME -- input the exported results to calculate the electronic-transition matrix elements

