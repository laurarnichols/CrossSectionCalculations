# Triply hydrogenated Si vacancy calculation for GaN Paper

This calculation considers the +/0 transition for a triply hydrogenated vacancy in Si. The same transition was considered in the Barmparis paper, but the geometry used for the defect supercell was not correct, the charge state was set using jellium, spin polarization was not used, everything was done at the PBE level, and only eigenvalue differences were used. 

For this calculation, I will need the ground-state, perfect-crystal system; the excited-state, positive-defect system; and the ground-state, neutral-defect system. 

_Note: Andy mentioned in the past that with WZP, we need to confirm that the states we are placing the carriers in are not resonance states. He said to do this by generating `PARCHG` files. I don't remember how to do this off of the top of my head, but it's theoretically something that should be done for these calculations if we have time._

## Tasks
- [X] [VASP and Export](./VASPAndExport/) 
- [X] [Group velocity](./VASPandExport/pristine/groupVelocity/)
- [X] [Energy tabulator](./posToNeut/EnergyTabulator/)
- [X] [Phonons](./Phonons)
- [X] [Phonon post-processing](./posToNeut/PhononPP)
- [X] Zeroth-order
  - [X] [Matrix elements](./posToNeut/zerothOrder/TME)
  - [X] [Transition rate](./posToNeut/zerothOrder/LSF)
- [X] First-order
  - [X] [Matrix elements](./firstOrder/TME)
  - [X] [Transition rate](./firstOrder/LSF)
- [X] [Post-processing and plotting](./results)

## Results

The plots and the notebooks used to generate them are in the [results](./results) folder. Here are the final results with a 4x4x4 supercell and a 3x3x3 grid for the zeroth-order term and $\Gamma$-only for the first-order term. 

<p align="center">
  <img src="./results/SiVH3_0th1st_posToNeut_20231213Laura.png" width="50%">
</p>

