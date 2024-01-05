# Ground state N antisite defect

## 3x2x2 supercell

I started from the [relaxed pristine supercell](../pristine/) and removed Ga atom 7 near the center of the cell (`0.500000000         0.583333313         0.499429911`), replaced it with a N atom (cut and pasted it to the bottom of the file and updated the atom numbers), then shifted the N position slightly (`-0.01 0.01 -0.02` in direct coordinates) to break the symmetry. Going to relax and make sure that the N atom doesn't go back to the higher-symmetry position. 

I kept the $\Gamma$-only k-point mesh but turned spin polarization on for the defect supercell. Only relaxed the inner DOF.

I got a relaxed structure, but it is really close to one of the N atoms. I think I might start over and first let the whole structure relax symmetrically then break the symmetry. I will keep track of the energies though. 

| Start | End | Energy (eV) | Description |
|-------|-----|-------------|-------------|
| [`POSCAR1_3x2x2`](./POSCAR1_3x2x2) | [`CONTCAR1_3x2x2`](./CONTCAR1_3x2x2) | -578.23890851 | Shift before relaxing |
| [`POSCAR2_3x2x2`](./POSCAR2_3x2x2) | [`CONTCAR2_3x2x2`](./CONTCAR2_3x2x2) | -578.29380991 | Relax without shifting |

The first configuration where I shifted first resulted in a dimer-like configuration with two N atoms bonded with a bond length of 1.27 A. This is similar to what (I think) the result was in [Gao 2004 Intrinsic](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.70.245208). That paper says the optimal position they got for the N antisite defect was 
> a N-N$\langle 0001 \rangle$ split configuration along the c axis, leaving a Ga vacancy at the original site... The bond distance between the two atoms of the N-N split configuration is about 1.31 A, which is comparable to the bond length in a N$\_2$ molecule... the remaining bond lengths to the e-type neighbors increase from the ideal value of 1.9 A to a value 2.2 A.

The N$\ _2$ bond length is 1.09 A, so I guess they are just saying that the atoms prefer to be closer than the default position?

But if I relax the system without shifting first, I still get to a configuration that breaks symmetry, just not as much. The N atoms that are close to each other (atoms 55 and 96) in the other configuration actually end up in the same positions, but there is an additional atom (76) close to the N antisite, also with a smaller bond length at 1.44 A. This configuration has a smaller energy than the first, but it does not line up with the paper.

I showed the new configuration to Sok and he said it could be feasible that I could find a new lower-energy configuration because computers are more powerful now, but he suggested using a larger supercell size for higher accuracy, so I moved to using the 5x3x3 supercell.

## 5x3x3 supercell

Similar to the 3x2x2 supercell, I relaxed the pristine cell then removed Ga atom 167 near the center of the supercell (`0.60000   0.44445   0.49968`) and replaced it with a N atom. To start, I am not going to break the symmetry before relaxing to see if I will get a similar configuration to what I saw in the 96-atom supercell. For consistency, I will name this `POSCAR2_5x3x3`.

In anticipation of the larger supercell taking a lot longer, I switched to using the $\Gamma$-only compilation of VASP for the relaxation. There is no loss of accuracy; it just takes into account simplifications available with just the $\Gamma$ point. Our `Export` code is not yet implemented to get the wave functions for $\Gamma$-only, so we will need to either implement that or use the standard version to get the wave functions. Implementing that will be one of my top priorities moving forward.

| Start | End | Energy (eV) | Description |
|-------|-----|-------------|-------------|
| [`POSCAR1_5x3x3`](./POSCAR1_5x3x3) | [`CONTCAR1_5x3x3`](./CONTCAR1_5x3x3) | -2182.24869595 | Shift before relaxing |
| [`POSCAR2_5x3x3`](./POSCAR2_5x3x3) | [`CONTCAR2_5x3x3`](./CONTCAR2_5x3x3) | -2182.20953186 | Relax without shifting |

Resulting geometry without shifting is similar to that seen in the 96-atom supercell, with the central N being bonded closely to two other N atoms at distances 1.44 and 1.45 A.

I also set up a shifted version of the larger supercell, where the N antisite atom is shifted by a small amount away from the high-symmetry position (`-0.01 0.01 -0.02` in direct coordinates). Just as in the smaller supercell, the displaced version ends up with a geometry matching that in the literature, with two N atoms close together at a distance of 1.26 A. However, in the smaller supercell and in the literature, the pair of atoms points in the c direction, while the pair in my system points along the original Ga-N bond direction, with the Ga replaced by the antisite N atom and the bond length shortened. 

To see if this change is responsible for the 2-atom configuration being lower in the larger supercell as compared to the smaller supercell, I set up the resulting configuration of the N atoms from the smaller supercell and the literature in the larger supercell. 