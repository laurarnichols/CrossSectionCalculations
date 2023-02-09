# Triply hydrogenated Si vacancy calculation for GaN Paper

This calculation considers the +/0 transition for a triply hydrogenated vacancy in Si. The same transition was considered in the Barmparis paper, but the geometry used for the defect supercell was not correct, the charge state was set using jellium, and everything was done at the PBE level. 

For this calculation, I will need the ground-state, perfect-crystal system; the excited-state, positive-defect system; and the ground-state, neutral-defect system. For the defect system, the geometry should be relaxed in the positive defect state. 

_Note: Andy mentioned in the past that with WZP, we need to confirm that the states we are placing the carriers in are not resonance states. He said to do this by generating `PARCHG` files. I don't remember how to do this off of the top of my head, but it's theoretically something that should be done for these calculations if we have time._

### 0/- transition

Guanzhi did the 0/- charge-state transition. He used a 2x2x2 supercell with a 5x5x5 k-point grid for his calculations because HSE and excited-state DFT calculations and the first-order matrix element calculations are not feasible in larger supercells. The first-order matrix elements require derivatives along each of the phonon directions, so they size of the calculations increases rapidly with supercell size. _Note: I am curious what portion of this calculation size was due to how incredibly slow the Export program previously was. That is something to possibly consider in the future now that the program is much faster._ 

He calculated the zeroth-order matrix element using a 5x5x5 supercell with a 2x2x2 k-point mesh, where the defect was in the ground state (neutral), in order to justify the use of the 2x2x2 supercell. His results showed that the larger and smaller supercells gave the same results for the zeroth-order matrix elements. Because he used the ground state for the 5x5x5 supercell, he also used it for the 2x2x2 supercell. Technically, because he considers the 0/- transition, his final state for the matrix element should be the negatively-charged defect in the neutral-defect-relaxed positions; however, Xiaoguang and Sok said that the wave functions probably would not change for the two charge states and that the choice is justified given that the excited-state calculations are so much more difficult to converge. 

The excited-state calculations must still be used for the first-order term for this transition and for the relaxation of the +/0 transition. The WZP paper does not address using multiple k-points. Xiaoguang argued that the band carriers are just screening charges and, since the energy is subtracted out in the WZP method, the final results do not change significantly if the carriers are excited across the k-points in order of increasing energy (taking into account the band dispersion) or uniformly across k-points. He also said that exciting them uniformly was simpler and easier to converge, so that is the method we use.

In the calculations, Guanzhi treated the perfect crystal as spin-polarized (`ISPIN=2`) even though that's not needed because he said it made it easier to match the output up with the defect results. I will use `ISPIN=1` for the perfect crystal and update the output files manually. He also used `ISYM=-1` to avoid mistakes, but the Export code handles the weight of the k-points with `ISYM=0`, so that is what I will use. With `ISYM=0`, the VASP Wiki says not to use the Monkhorst-Pack k-point mesh (what Guanzhi used), so I will use a gamma-centered grid. These changes should not affect the results and should just make them faster. 

### Barmparis paper

In the Barmparis paper, the process for the DFT calculations was to relax at the Gamma point then do an NSCF calculation to get to a denser k-point mesh. However, the supercell used there was slightly larger (216 vs 64 atoms). I will start with relaxing with the full mesh (5x5x5 in 2x2x2 supercell) and worry about using the process outlined in the Barmparis paper calculations if the relaxation is too slow.

## Tasks

### Zeroth-order matrix elements
- [ ] Perfect crystal 2x2x2 supercell, 5x5x5 k-point mesh
  - [x] Relax
  - [x] SCF (tighter convergence, symmetry off)
  - [ ] Export (need to make output seem spin-polarized even though they aren't)
- [ ] Defect crystal 2x2x2
  - [ ] Relax defect in ground state (neutral)
  - [ ] SCF for ground state defect
  - [ ] Excite carrier out of defect into band and re-relax
  - [ ] SCF for excited state
  - [ ] SCF for ground state at excited-state positions
  - [ ] Export
- [ ] Get matrix elements with `TME`
- [ ] Plot results

### Phonons

???

### $S_j$

???

### First-order matrix elements

???

## Notes and questions from Guanzhi's input files

* I remember Guanzhi and Xiaoguang saying that we don't use binning anymore, so does that mean the `TME` code has been updated?
* I don't know how to run the rest of the calculations, so I'm not sure what DFT calculations are needed to feed into them.
* Will set up the calculations I know I need for the zeroth-order matrix elements then go through his files/email him to figure out what other steps are needed. 
* Guanzhi still needs to send the flow chart for how to run our code.
