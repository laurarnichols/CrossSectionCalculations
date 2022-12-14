# SiVH3 Pristine

216-atom pristine Si supercell. Ran relaxation 7 nodes.

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
  * PBE
  * Read in from SCF
  * All settings same as SCF but `ICHARG = 11`
