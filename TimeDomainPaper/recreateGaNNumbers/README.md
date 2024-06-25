# Recereate GaN Numbers

Because the numbers for GaN have changed a lot, I feel the need to recreate them in order to trust them. Because the relaxation took a while, and I want to be able to compare directly with Guanzhi's results, I am going to use his relaxed geometries (the same that I used to test the [overlap convergence](../GaNOverlaps/)). I am also using his VASP parameters:
```
ENCUT = 400
EDIFF = 1E-8
ISYM = -1
AEXX = 0.31
```

I asked Guanzhi what he did to get the $\Gamma$-only HSE wave functions since HSE does not allow for an NSCF calculation. He said that he used the 2x2x2 MP relaxed positions and did a $\Gamma$ SCF calculation. Xiaoguang said this was not correct. Instead, I did an SCF calculation with the 2x2x2 MP k-points listed explicitly and added $\Gamma$ with zero weight. Since I already did this for the pristine supercell and the ground-state relaxed positions, I will not need to recalculate those. 

## Zeroth-order 

### Plan

For the zeroth-order term, we need the overlap between the perfect crystal valence-band states and the final defect state from the final charge state of the defect (ground state) in the initial-state relaxed positions. I will also need total energies for the relaxed final state, the relaxed initial state, and the final charge state in the initial positions in order to calculate all of the energies that I need. 

I will also need the HSE 2x2x2 MP phonons. Finally, I will need to run the LSF code to get the transition rate using
```
dt = 5e-9 ! ps
hbarGamma = 3.7 ! meV
smearingExpTolerance = 1e-5
```
based on the numbers given in the paper (I will not retest the convergence of these parameters). I will also need to run this for `temperature = 50,100,200,300,400,500,600,700,800` (estimated temperatures that Guanzhi used based on the plot).

### Calculations

Rather than calculate them from scratch, Guanzhi sent me the relaxed excited-state positions and the initial and final phonons. At first glance of the files, I realized that we could not combine the phonons as-given because the modes are sorted by increasing frequency and they do not line up between the files. I have updated the `PhononPP` code to line up the modes properly by maximizing the dot product bewteen the phonon eigenvectors. I tested it using the Si inputs, with the same phonon file input twice, and it worked as expected: dot product with the same mode is 1 and with other modes is 0. 

As a check, I recalculated the total energy (`-736.95474968`) for the excited-state positions that Guanzhi sent and got the same values. I also got nearly degenerate values for the bands involved in the carrier excitation, as Guanzhi did. 

When looking at the eigenvalues and occupations for $\Gamma$, I realized that the occupations were not correct. After looking into it more, I found [this wiki article](https://www.vasp.at/wiki/index.php/Band-structure_calculation_using_hybrid_functionals) that discussed issues with converging zero-weight k-points. Because of this, I reached out to Guanzhi to ask what he did and if he tested the convergence of the wave functions. He said that he used `EDIFF = 1E-8` and that the wave functions were orthonormal. I will need to update my energy convergence criterion to match his and test the convergence as well. I did not use that tight of convergence for the initial-state SCF, but I think that is okay because we are not using those wave functions. I am going to go ahead and redo the final-state relaxed SCF calculation as well with only the 2x2x2 MP grid since we don't need those wave functions, and I am more confident in that approach.