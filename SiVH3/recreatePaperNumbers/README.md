# Recreate Paper Matrix Elements in VASP

The goal of this set of calculations is to calculate the matrix elements doing exactly what the Barmparis paper did but use VASP instead of QE.

For the zeroth-order matrix element, we only need the initial state (neutral pristine) and the final state (ground-state defect). We consider electron capture by a triply-hydrogenated Si vacancy in bulk Si. In the initial (excited) state, the defect is positively charged, while it is neutral in the final (ground) state.

In the original paper, the geometry of each system (pristine, neutral defect, charged defect) were optimized independently. However, we should really be considering a vertical transition, so the final defect wave function should be taken from the system with the initial atomic positions (from positively-charged defect) and final (neutral) charge state. Because I am trying to validate our code and recreate the paper numbers, I am going to do what the paper did here. However, I am also going to do a calculation to see what difference is made by using the correct wave functions. 

## Tasks

I will need to do calculations on the perfect-crystal supercell and the final state of the defect with an electron captured. For each system, I will do a relaxation, an SCF calculation to converge the charge density based on the final ion positions (with more bands and tighter convergence), and an NSCF calculation to increase the k-point grid (with `ISYM = 0`). I will then need to export each and run the TME program to get the matrix elements.

- [x] [Neutral pristine](./VASP/pristine/)
  - [x] Relax (including cell)
  - [x] SCF
  - [x] NSCF
  - [x] [Export](./Export)
- [x] [Neutral defect](./VASP/finalChargeState/finalPositions/) (final, ground state)
  - [x] Relax (only inner dof)
  - [x] SCF
  - [x] NSCF
  - [x] [Export](./Export)
- [x] Run [TME](./TME/)
- [x] Plot results

## Results

Final results:

<p align="center">
  <img src="./VASPvsPaper.png" width="50%">
</p>

Originally, the results from VASP were about twice as big as those from the paper. The absolute difference wasn't that large, but the `Export` code as it was was very inefficient and slow and had issues with the ordering of the G-vectors. I fully merged our two Export programs and fixed the bugs, and now the results match those from the paper. 
