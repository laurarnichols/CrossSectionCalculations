# Recreate Paper Matrix Elements in VASP

The goal of this set of calculations is to calculate the matrix elements doing exactly what the Barmparis paper did but use VASP instead of QE.

For the zeroth-order matrix element, we only need the approximate initial state (neutral pristine) and the final state (ground-state defect). The language that we currently use (neutral vs charged) refers to the defect, but previous input files referred to the supercell. So the neutral-cell calculation from the original paper includes a negatively-charged defect, and the charged-cell calculation (+1) refers to a neutral defect.

In the original paper, the geometry of each system (pristine, neutral defect, charged defect) were optimized independently. However, we should really be considering a vertical transition, so the final defect wave function should be taken from the system with the initial atomic positions (from neutral defect) and final (negative) charge state. Because I am trying to validate our code and recreate the paper numbers, I am going to do what the paper did here. However, I am also going to do a calculation to see what difference is made by using the correct wave functions. 

## Tasks

I will need to do calculations on the perfect-crystal supercell and the final state of the defect with an electron captured. For each system, I will do a relaxation, an SCF calculation to converge the charge density based on the final ion positions (with more bands and tighter convergence), and an NSCF calculation to increase the k-point grid. I will then need to export each and run the TME program to get the matrix elements.

- [ ] Neutral pristine
  - [x] Relax
  - [x] SCF
  - [ ] NSCF (started)
  - [ ] Export
- [ ] Negatively-charged defect with neutral supercell (final, ground state)
  - [ ] Relax
  - [ ] SCF
  - [ ] NSCF
  - [ ] Export
- [ ] Run TME
- [ ] Plot results

