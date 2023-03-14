# Triply hydrogenated Si vacancy calculation for GaN Paper

This calculation considers the +/0 transition for a triply hydrogenated vacancy in Si. The same transition was considered in the Barmparis paper, but the geometry used for the defect supercell was not correct, the charge state was set using jellium, spin polarization was not used, and everything was done at the PBE level. 

For this calculation, I will need the ground-state, perfect-crystal system; the excited-state, positive-defect system; and the ground-state, neutral-defect system. For the defect system, the geometry should be relaxed in the positive defect state. 

_Note: Andy mentioned in the past that with WZP, we need to confirm that the states we are placing the carriers in are not resonance states. He said to do this by generating `PARCHG` files. I don't remember how to do this off of the top of my head, but it's theoretically something that should be done for these calculations if we have time._

### 0/- transition

Guanzhi did the 0/- charge-state transition. He originally used a 2x2x2 supercell with a 5x5x5 k-point grid for his calculations because they said HSE and excited-state DFT calculations and the first-order matrix element calculations are not feasible in larger supercells. The first-order matrix elements require derivatives along each of the phonon directions, so they size of the calculations increases rapidly with supercell size. After parallelizing the TME and Export codes and running some of the calculations myself, Sok and I argued that we should try using a bigger supercell for the matrix elements. We ended up deciding on a 4x4x4 supercell at the Gamma point for the matrix elements and a 2x2x2 supercell with a 3x3x3 k-point mesh for the phonons. The phonons in the smaller supercell are directly applied to the larger supercell to displace the atoms for the first-order matrix elemtns. 

Guanzhi originally considered the ground-state defect in the relaxed positions of the neutral defect for all of the matrix elements. Technically, because he considers the 0/- transition, his final state for the matrix element should be the negatively-charged defect in the neutral-defect-relaxed positions; however, Xiaoguang and Sok said that the wave functions probably would not change for the two charge states and that the choice is justified given that the excited-state calculations are so much more difficult to converge. He later came back and said something about using the final charge state, but I tried to clarify and have not gotten a response.

In the calculations, Guanzhi treated the perfect crystal as spin-polarized (`ISPIN=2`) even though that's not needed because he said it made it easier to match the output up with the defect results. I will use `ISPIN=1` for the perfect crystal because I updated the Export and TME codes to consider spin-polarization properly. He also used `ISYM=-1` to avoid mistakes, but the Export code handles the weight of the k-points with `ISYM=0`, so that is what I will use. With `ISYM=0`, the VASP Wiki says not to use the Monkhorst-Pack k-point mesh (what Guanzhi used), so I will use a gamma-centered grid. These changes should not affect the results and should just make them faster. 

### Barmparis paper

## Tasks
- [X] [Perfect crystal](./VASP/pristine) 
- [ ] [Defect crystal](./VASP/defect)
- [ ] [Get overlaps with `TME`](./TME)
- [X] [Final charge state/final positions phonons](./Phonons)
- [ ] $S_j$
- [ ] $M_j$
- [ ] Zeroth-order capture coefficient
- [ ] First-order capture coefficient

## Notes and questions from Guanzhi's input files

* I remember Guanzhi and Xiaoguang saying that we don't use binning anymore, so does that mean the `TME` code has been updated?
* I don't know how to run the rest of the calculations, so I'm not sure what DFT calculations are needed to feed into them.
* Will set up the calculations I know I need for the zeroth-order matrix elements then go through his files/email him to figure out what other steps are needed. 
* Guanzhi still needs to send the flow chart for how to run our code.
