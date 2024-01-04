# Ground state N antisite defect

## 3x2x2 supercell

I started from the [relaxed pristine supercell](../pristine/) and removed Ga atom 7 near the center of the cell (`0.500000000         0.583333313         0.499429911`), replaced it with a N atom (cut and pasted it to the bottom of the file and updated the atom numbers), then shifted the N position slightly to break the symmetry. Going to relax and make sure that the N atom doesn't go back to the higher-symmetry position. 

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

Similar to the 3x2x2 supercell, I relaxed the pristine cell then removed Ga atom 167 near the center of the supercell (`0.60000   0.44445   0.49968`) and replaced it with a N atom. To start, I am not going to break the symmetry before relaxing to see if I will get a similar configuration to what I saw in the 96-atom supercell. 