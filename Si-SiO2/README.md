# $\text{Si}$ / $\text{SiO}\_2$ Interface and H Release

The structure that Blair sent is an interfacial model without (as far as I can tell) any dangling bonds. Based on Andy's suggestion, I am going to strain the cell in the $a$ and $b$ directions to match the Si lattice constant (5.43 A). The $a$ and $b$ directions are along the diagonal of a face of the Si unit cell. There are 3 atoms along the diagonal in the unit cell, with a total distance of $5.43\sqrt{2} = 7.679$ A. There are 4 atoms across the $a$ and $b$ directions of the supercell, so the $a$ and $b$ lattice constants should be 15.358 A. The strained CONTCAR with the new lattice constants is stored in `CONTCAR_strained`.

## Preliminary relaxation

Before doing parameter convergence tests, I will need to relax the newly-strained supercell. I will relax using a special compilation of VASP that only relaxes the cell in the c-direction (for details on this see the [Relaxation](../Notes/VASPFlagsAndCalculations.md#relaxation) section in the VASP Flags and Calculations note). For this initial relaxation, I will use the following parameters:
* 2x2x1 `KPOINTS` grid
* `ENCUT = 1.3*max(ENMAX) = 520` eV
* `EDIFF = 1E-5` eV
* `PREC = Normal`
* `ISPIN = 1`
* `EDIFFG = -1E-2` eV/A
* `SIGMA = 0.001`
