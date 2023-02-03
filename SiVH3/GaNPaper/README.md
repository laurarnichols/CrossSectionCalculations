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

## Notes and questions from Guanzhi's input files

* 5x5x5 supercell
  * This large supercell is generated from a relaxed 3x3x3 supercell padded by perfect crystal using `gen supercell`
  * Perfect crystal
    * `ENCUT` is 400 eV
    * `ENMAX` in `POTCAR` file is 245.345 eV, so 400 eV seems reasonable
    * Does it need to be the same as what is used in the defect cell? I would think so for the matrix element calculations.
    * `NBANDS` is 3008
    * `EDIFF = 1E-6`. Is that converged?
    * The Barmparis calculations used `ISYM=0`. Why is `ISYM=-1` used here?
    * HSE part is commented out. Where is HSE used?
    * `ISPIN=2` here for spin-polarized, but I don't think that is needed for the perfect crystal
    * Why is the Monkhorst-Pack scheme used rather than a $\Gamma$-centered grid? VASP wiki says only use $\Gamma$-centered for FCC with `ISYM>=0`.
    * 2x2x2 k-point grid is used
  * Defect 
    * Same inputs as perfect crystal but different geometry
    * Will need to relax in positive charge state
    * Only included neutral state, which should be his initial/my final state
    * If 5x5x5 supercells are used for the electronic matrix elements, shouldn't the defect state be negative here for the transition that Guanzhi is considering?
