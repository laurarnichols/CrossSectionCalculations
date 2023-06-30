# Triply hydrogenated Si vacancy calculation for GaN Paper

This calculation considers the +/0 transition for a triply hydrogenated vacancy in Si. The same transition was considered in the Barmparis paper, but the geometry used for the defect supercell was not correct, the charge state was set using jellium, spin polarization was not used, and everything was done at the PBE level. 

For this calculation, I will need the ground-state, perfect-crystal system; the excited-state, positive-defect system; and the ground-state, neutral-defect system. 

_Note: Andy mentioned in the past that with WZP, we need to confirm that the states we are placing the carriers in are not resonance states. He said to do this by generating `PARCHG` files. I don't remember how to do this off of the top of my head, but it's theoretically something that should be done for these calculations if we have time._

## Tasks
- [ ] [VASP and Export](./VASPAndExport/) 
- [ ] [Phonons](./Phonons)
- [ ] [Phonon post-processing (`Sj` and `Shifter`)](./PhononPP)
- [ ] Zeroth-order
  - [ ] [Matrix elements](./zerothOrder/TME)
  - [ ] [Transition rate](./zerothOrder/LSF)
- [ ] First-order
  - [ ] [Matrix elements](./firstOrder/TME)
  - [ ] [Transition rate](./firstOrder/LSF)
- [ ] Post-processing and plotting

## Results

The plots and raw data are in the [results](./results) folder. Here are the raw results with a 4x4x4 supercell and a gamma-only grid, showing how there are significant gaps in the energy levels with just one k-point.

<p align="center">
  <img src="./results/4x4x4Gamma.png" width="50%">
</p>

