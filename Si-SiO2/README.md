# $\text{Si}$ / $\text{SiO}_{2}$ Interface and H Release

*The goal of these calculations was to relax the $\text{Si}$/$\text{SiO}_{2}$ interface to consider a hydrogenated dangling bond at the interface. Working with amporphous $\text{SiO}_{2}$ was to difficult, so we decided to pivot to GaN.* 

The structure that Blair sent is an interfacial model without (as far as I can tell) any dangling bonds. Based on Andy's suggestion, I am going to strain the cell in the $a$ and $b$ directions to match the Si lattice constant (5.43 A). The $a$ and $b$ directions are along the diagonal of a face of the Si unit cell. There are 3 atoms (two bond lengths) along the diagonal in the unit cell, with a total distance of $5.43\sqrt{2} = 7.679$ A. There are 5 atoms (4 bond lengths) across the $a$ and $b$ directions of the supercell, so the $a$ and $b$ lattice constants should be 15.358 A. The strained CONTCAR with the new lattice constants is stored in `CONTCAR_strained`.

## Preliminary relaxation

Before doing parameter convergence tests, I will need to relax the newly-strained supercell. I will relax using a special compilation of VASP that only relaxes the cell in the c-direction (for details on this see the [Relaxation](../Notes/VASPFlagsAndCalculations.md#relaxation) section in the VASP Flags and Calculations note). For this initial relaxation, I will use the following parameters:
* 2x2x1 `KPOINTS` grid
  * I tried to run this calculation using only the gamma point (based on Sok's direction), but the variable-cell relax was diverging with only a single k-point. 
  * Going to use 2x2x1 grid for relaxing the cell in the ground state, then try to do a fixed-cell relax at the Gamma point for the other calculations.
* `ENCUT = 1.3*max(ENMAX) = 520` eV
* `EDIFF = 1E-5` eV
* `PREC = Normal`
* `ISPIN = 1`
* `EDIFFG = -1E-2` eV/A
* `SIGMA = 0.001`
