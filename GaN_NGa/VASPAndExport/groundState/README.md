# Ground state N antisite defect

I started from the [relaxed pristine supercell](../pristine/) and removed a Ga atom near the center of the cell, replaced it with a N atom, then shifted the N position slightly to break the symmetry. Going to relax and make sure that the N atom doesn't go back to the higher-symmetry position. 

I kept the $\Gamma$-only k-point mesh but turned spin polarization on for the defect supercell. Only relaxed the inner DOF.

I got a relaxed structure, but it is really close to one of the N atoms. I think I might start over and first let the whole structure relax symmetrically then break the symmetry. I will keep track of the energies though. 

| Start | End | Energy (eV) | Description |
|-------|-----|-------------|-------------|
| [`POSCAR1`](./POSCAR1) | [`CONTCAR1`](./CONTCAR1) | -578.23884415 | Shift before relaxing |