# Pristine Si

216-atom pristine Si supercell. Ran on 7 nodes (308 processors) on Onyx.
Calculations:
* Relax
  * Gamma point
  * PBE
  * Relax the supercell (`ISIF = 3`)
* SCF
  * Gamma point
  * PBE
  * Read in from relaxation
  * Set bands (800)
  * Tighten `EDIFF` (`1E-7`)
* NSCF
  * 3x3x3 k-point grid
  * Turn of k-point symmetry using `ISYM = 0`
  * PBE
  * Read in from SCF
  * All settings same as SCF but `ICHARG = 11`
