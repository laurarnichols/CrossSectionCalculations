# Energy tabulation

There are many different energies needed for different parts of the calculation. Instead of needing to read the export files in multiple different places and calculate all of the different energies in different places, this program tabulates all of the different energies needed. 

Ideally, we would like to use everything from the HSE level, but we compromised for the gamma-point calculation and used PBE wave functions and HSE energy levels. However, the gamma-point calculation was not sufficient, so we needed to use a 3x3x3 mesh, but HSE energy levels would be expensive with 27 k-points (1 k-point took about 14 hours). Instead, we plan to use the PBE energy levels with potential corrections, assuming that the eigenvalue differences within the bands is okay. __The difference between HSE and PBE eigenvalue differences in reference to the CBM range from 0.05-2.5 meV.__ We will still use the HSE total energies. 

