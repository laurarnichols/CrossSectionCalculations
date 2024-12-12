# H Release Calculations in GaN

## Defect Exploration
First, I converged the perfect-crystal GaN calculations, first in the [primitive cell](./GaN/primitive/), then in the [pristine supercell](./GaN/pristine/). I then set up a N antisite defect because Sok thought that would be the easiest defect to work with. 

### $\text{N}_\text{Ga}$

The files for my calculations with the N antisite defect are in the [GaN_NGa](./GaN_NGa/) folder. I had to do multiple relaxations with that defect because I was getting a geometry with a slightly lower energy than the one in the literature. I was also getting several configurations of complexes (dimer/trimer + vacancies), which could complicate things.

I brought up with the group, however, that the formation of the antisite is very large--so much so that many papers do not consider it in detail. I proposed a few other alternatives and we landed on the O substitutional defect on a N site as the formation energy is low and there is threshold-voltage-shift data attributed to that defect.

### $\text{O}_\text{N}$ substitutional defect

I investigated this defect and found that the H does not bind to the $\text{O}_\text{N}$ defect. The energy of H far away from the defect is much lower than most configurations with H bonded to the defect. There is a low-energy configuration of H bonded to O with the O shifted into a DX-center-like position. However, that displacement is not stable in GaN, and the phonons resulted in an imaginary-frequency mode (i.e., the system is not stable along that mode vibration). In AlGaN, however, the DX-center can be stabilized because of the increased strain in the lattice, so this defect may be useful to consider in AlGaN. Previous treatment in experimental papers was done in AlGaN.

### $\text{V}_\text{Ga}$ 

Next, we tried and settled on a Ga vacancy with a single hydrogen. The vacancy is relatively simple, and is relevant in many defect papers. We were also able to identify the dangling-bond states and exclude them from consideration.

## Simplifications and open questions
We originally wanted to do electron capture, but that would involve scattering between $k$-points in the supercell, which we did not have time to figure out how to do. Instead, we looked at hole scattering since the valence bands are more dense and shallow. We also assume that the electron is in the vacinity of the defect when it gets perturbed. We closed our eyes to the extent of the electron wave function and did not consider wave packets or actual motion of the electron, and we only treated GaN. 

For a more in-depth consideration of this problem, we would need to consider electron scattering. Also, we would need to figure out how to treat defects in the AlGaN layer that perturb electrons in the GaN channel. We would also need to consider a denser sampling of the energy space through the use of more $k$-points. 

## Calculation Steps
Prior to these calculations, I converged VASP parameters in the primitive cell. I ended up using `ENCUT = 520`, `EDIFF = 1e-6`, and `AEXX = 0.29`. I didn't end up using HSE calculations, though. 

* Relax ground state defect configuration (had from previous defect exploration step).
* Relax each band state, then SCF for accurate total energy.
    * I used jellium here to remove the charge and constrained DFT to place the carrier in each individual band.
    * Not all of the states converged, so I only included those that I was able to converge with a reasonable amount of effort.
* Perform an additional SCF in ground electronic state for each set of relaxed positions. Need this to isolate just the relaxation energy.
* Relax perfect crystal, then SCF to get wave functions and accurate eigenvalues.
* Export perfect-crystal and ground-state wave functions along with energies from relaxed excited states and excited-state.positions in electronic ground state
* Use TME to line up bands in defect and perfect-crystal systems.
    * We determined that the band shift needed to line up the valence band edge in the perfect crystal and defect crystal systems was `ibShift_braket = 7`.
    * We are looking to maximize the total overlap.
    * This process took manual examination because there was a localized dangling bond state.
    * Start with a first pass with all bands included. 
    * Look at resulting maximum overlap and find bands that look like a really bad match ($\ll 1$).
    * Go back and forth between `optimalPairs.out` and `allElecOverlap` files to try to manually adjust matches.
    * Keep in mind that bands should not shift far in energy unless you want to exclude them from consideration.
* Tabulate energies using `EnergyTabulator`.
    * Bands are labeled according to optimal pairs from `TME`.
    * Eigenvalues come from perfect crystal.
    * Total energies are extracted from relaxed ground state and relaxed excited state in ground electronic configuration.
    * I allowed for negative energy transfer to consider all possible transitions, but didn't allow zero energy transfer since matrix elements would be zero. I used `dENegThresh = 1e6` and `dEZeroThresh = 1e-6`.
    * I isolated my consideration to bands 1546-1613.
    * Use same shift of the bands, `ibShift_eig`, as used in `TME` for `ibShift_braket`.
    * The reference band for calculating eigenvalues relative to was the valence band (1613).
* Run `PhononPP` 
    * Use `T = 300` K for setting base occupations.
    * Point to the `EnergyTabulator` output and `optimalPairsDir` to make sure that states are consistently labeled. Only states included in the energy table will be considered from here on.
    * Input relaxed excited state and relaxed ground state geometries to calculate all displacements upon carrier approach, transition, and departure for each possible initial and final state.
* Run `TME` with energy table and optimal pairs to get all needed matrix elements.
* Run `LSF` to get updated occupations
    * I did not include the `deltaNj` adjustments after carrier approach when calculating the transition rates. I tested it and didn't see a difference for this case, and it makes the calculations much slower.
    * I used `generateNewOccupations = .true.` to get new occupations for each step to input into the rogue-waves code.
    * I used and validated `energyAvgWindow = 1e-2` eV.
    * I used `thermalize = .true.` to generate a new temperature at each step rather than channeling the energy into modes harmonically.
    * For the integration over temperature (or time by proxy), I used
        * `nRealTimeSteps = 25`
        * `maxIterPerTimeStep = 15`
        * `tolForStepConverge = 2.0` K
        * `maxDeltaPerTimeStep = 15.0` K
        * `dt = 1e-3` s (this will be decreased automatically to meet max delta criteria)
    * For the time-domain integration to get the transition rate at each step, I used
        * `dtau = 5e-3` $\hbar / E_{\text{H}}$
        * `hbarGamma = 3.7` meV
        * `smearingExpTolerance = 5e-5`
    * Input results from previous codes along with carrier density from device.
* Input each set of occupations into the rogue-waves code and set a bond-cutoff threshold to get the exceedance probability.
* Calculate the rate of change of the probability at each step to determine `r(T)` (see Analysis notebook).