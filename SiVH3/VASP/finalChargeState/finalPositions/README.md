# SiVH3 Neutral Defect in Neutral Positions

218-atom Si supercell with triply-hydrogenated Si vacancy in the center of the cell. Charge state is neutral and relaxed in neutral charge state.  Ran on 7 nodes (308 processors) on Onyx.

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
