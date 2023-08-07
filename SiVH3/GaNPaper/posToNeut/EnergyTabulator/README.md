# Energy tabulation

There are many different energies needed for different parts of the calculation. Instead of needing to read the export files in multiple different places and calculate all of the different energies in different places, this program tabulates all of the different energies needed. 

Ideally, we would like to use everything from the HSE level, but we compromised for the gamma-point calculation and used PBE wave functions and HSE energy levels. However, the gamma-point calculation was not sufficient, so we needed to use a 3x3x3 mesh, but HSE energy levels would be expensive with 27 k-points (1 k-point took about 14 hours). Instead, we plan to use the PBE energy levels with potential corrections, assuming that the eigenvalue differences within the bands is okay. __The difference between HSE and PBE eigenvalue differences in reference to the CBM range from 0.05-2.5 meV.__ We will still use the HSE total energies. To compare, I have included the energy tables for the gamma point when using HSE total energies and eigenvalues (`HSEOnly`) and when using HSE total energies and PBE eignvalues with the correction below (`HSEAndPBE`). When comparing these levels, I used the PBE calculation with a gamma-only grid, but the export of the 3x3x3 PBE calculation was used for the eigenvalues for the full 3x3x3 calculation. 


## Energy corrections

* I do not need a correction on the zeroth-order energy because my reference carrier is in the CBM.
* We are not currently doing a first-order calculation, but I am going ahead and getting the correct energy value just in case.
* For the first-order energy at gamma, I need a correction:
```f90
! eCorrectEigF = [eigCBM_HSE - eigF_HSE] - [eigCBM_HSE - eigF_HSE]

eigCBM_PBE = 2.293901362260629E-001 ! Hartree
eigF_PBE = 2.151828316319239E-001   ! Hartree
eigCBM_HSE = 2.368450976083232E-001 ! Hartree
eigF_HSE = 2.029537049111589E-001   ! Hartree

eCorrectEigF = 0.5356 ! eV
```
* These values can be found by looking at the `eigenvalues.isp.ik` file for the right spin and k-point or by running `EnergyTabulator` with a zero energy correction and subtracting the first-order energy difference between HSE and PBE, then converting to eV.

The correction above is just for the gamma point, but there would presumably be some dispersion of the defect level in both PBE and HSE, so I am not sure that using the same energy correction across all of the k-points would be appropriate. It may be okay if we say that PBE systematically underestimates the gap between the defect level and the CBM so that we only need to use one k-point to find that error. But what about Guanzhi's case where his zeroth-order energy will need a correction for the energy of the initial state above the reference-carrier state? I am not sure how the supercell and k-point sampling combine to fold in the bands. How will the CBM at each k-point be affected? Is it okay to say that it is underestimated by a set value at every k-point? 
