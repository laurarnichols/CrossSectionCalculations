# Triply hydrogenated Si vacancy calculation for GaN Paper

This calculation considers the +/0 transition for a triply hydrogenated vacancy in Si. The same transition was considered in the Barmparis paper, but the geometry used for the defect supercell was not correct, the charge state was set using jellium, and everything was done at the PBE level. 

For this calculation, I will need the ground-state, perfect-crystal system; the excited-state, positive-defect system; and the ground-state, neutral-defect system. For the defect system, the geometry should be relaxed in the positive defect state. 

## Tasks

Tasks based on how things were done in the Barmparis paper (will need to be updated):

- [ ] Perfect crystal
  - [ ] Relax
  - [ ] SCF
  - [ ] NSCF
  - [ ] Export
- [ ] Positive-defect crystal (I think this may be used for phonons, but I'm not sure what needs to be done)
  - [ ] Relax
  - [ ] SCF
  - [ ] NSCF (?)
  - [ ] Export (?)
- [ ] Neutral-defect crystal
  - [ ] SCF using positive-defect geometry
  - [ ] NSCF
  - [ ] Export
