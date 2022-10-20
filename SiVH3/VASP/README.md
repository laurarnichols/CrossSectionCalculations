# Recreate Paper Matrix Elements in VASP

The goal of this set of calculations is to calculate the matrix elements doing exactly what the Barmparis paper did but use VASP instead of QE.

For the zeroth-order matrix element, we only need the approximate initial state (neutral pristine) and the final state (ground-state defect). The language that we currently use (neutral vs charged) refers to the defect, but previous input files referred to the supercell. So the neutral calculation from the original paper includes a negatively-charged defect, and the charged calculation refers to a neutral defect.

## Tasks

- [ ] Neutral pristine
  - [x] Relax
  - [ ] SCF (started)
  - [ ] NSCF
  - [ ] Export
- [ ] Negatively-charged defect with neutral supercell (final, ground state)
  - [ ] Relax
  - [ ] SCF
  - [ ] NSCF
  - [ ] Export
- [ ] Run TME
- [ ] Plot results

