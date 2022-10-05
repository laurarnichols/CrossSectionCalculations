# Check Hole Localization

In the Alkauskas paper, they spend a considerable amount of time on the choice of reference positions. They say that, in the charged-state equilibrium
positions, they do not see a clearly defined defect state for the negative charge state of the defect. Instead, they see "one or more diffuse
single-particle defect states that have moved down in energy and that couple strongly with bulk states." However, in the neutral-state equilibrium
positions, they see a well-defined defect state for both charge states of the defect. Therefore, they use the neutral-state equilibrium positions as
their reference positions. This choice, however, is questionable because we consider only the electronic transition and dissipation of that transition
energy, not the subsequent relaxation, so we should, in principle, be using the excited, charged-defect equilibrium positions.

When I brought up this concern with Xiaoguang, he said that they get a clearly-defined defect level in the charged-defect equilibrium positions and 
that they use those as the reference positions for the wave function and energy-level calculations. I brought up my concern that Alkauskas et al. got a 
different result and he said that it may be due to the fact that they use the jellium model (adding or removing an electron from the cell) while we use 
the WZP method (promoting an electron from the valence band and leaving the cell neutral). After discussion, we hypothesized that the main issue with
the jellium model could be that it does not localize charge correctly, so the electron and C do not see the localized hole charge that is present physically
and in the WZP model, resulting in an incorrect bound state. 

To test this hypothesis, I am going to do HSE calculations in the charged-state equilibrium positions using both the jellium model and the WZP method. I 
will compare the resulting equilibrium positions in each case and the charge-density distribution to see what differences are present and if they match
our hypothesis and explain the different results. I will also look at the bound state and the band state to ensure that they are sufficiently localized and 
diffuse, respectively.

I also want to see what the effect is of the band for the hole in the WZP method because Alkauskas et al. said that the third band down is the one that
couples most strongly to the defect, and Guanzhi said that was the one that he got to converge (at k = -0.21, -0.41, -0.21).

## Tasks

### Calculations

- [x] Relax primitive pristine cell at PBE level
- [x] Create 3x2x2 orthorhombic supercell
- [x] Ground state
  - [x] PBE
    - [x] Relax
    - [x] SCF
  - [x] HSE
    - [x] Relax
    - [x] SCF 
    - [x] Partial charge density
- [x] Excited state WZP/VBM
  - [x] PBE
    - [x] Relax
    - [x] Band calculation
  - [x] HSE
    - [x] Relax (waiting to see how jellium converges)
    - [x] SCF with tighter convergence criteria 
    - [x] Partial charge density
- [ ] Excited state WZP/3 down
  - [x] PBE
    - [x] Relax
    - [x] SCF
  - [ ] HSE
    - [x] Relax (waiting to see how jellium converges)
    - [ ] SCF with tighter convergence criteria
    - [ ] Partial charge density
- [ ] Excited state jellium
  - [x] PBE
    - [x] Relax
    - [x] SCF
  - [ ] HSE
    - [x] Relax (started)
    - [x] SCF with tighter convergence criteria
    - [ ] Partial charge density

### Results

| Electronic State | Functional | Excitation Model | Hole Location | $E_d  - E_{\text{VBM}}$ chan 1 (eV) | $E_d  - E_{\text{VBM}}$ chan 2 (eV) |
| --- | --- | --- | --- | --- | --- |
| Ground | PBE | - | - | 0.0448 | 0.1919 |
| Ground | HSE | - | - | 0.0313 | 1.5634 |
| Excited | PBE | WZP | VBM | 0.1233 | 0.0070 |
| Excited | HSE | WZP | VBM | | |
| Excited | PBE | WZP | 3 down | 0.089 | 0.1608 |
| Excited | HSE | WZP | 3 down | | |
| Excited | PBE | jellium | - | 0.1223 | 0.1223 |
| Excited | HSE | jellium | - | 0.0954 | 0.0954 |


### Analysis

- [x] Compare lattice parameters to Alkauskas
- [ ] Compare excited-state equilibrium positions (average atomic displacement vector)
  - [x] VBM vs 3 down, PBE/WZP (max=0.037 A, avg=0.009 A)
  - [ ] VBM vs 3 down, HSE/WZP
  - [ ] PBE vs HSE, 3 down/WZP
  - [x] PBE vs HSE, jellium (no difference)
  - [x] jellium vs WZP 3 down, PBE (max=0.012 A, avg=0.003 A)
  - [x] jellium vs WZP VBM, PBE (max=0.034 A, avg=0.007 A)
  - [ ] jellium vs WZP 3 down, HSE
  - [ ] jellium vs WZP VBM, HSE
- [ ] Compare energy of bound state above VBM
  - [ ] VBM vs 3 down, PBE/WZP
  - [ ] VBM vs 3 down, HSE/WZP
  - [ ] PBE vs HSE, 3 down/WZP
  - [ ] jellium vs WZP 3 down, HSE
  - [ ] jellium vs WZP VBM, HSE
  - [ ] ground vs excited, jellium/HSE
  - [ ] ground vs excited, WZP/HSE
- [ ] Compare charge density (charge density difference plot)
  - [ ] VBM vs 3 down, HSE/WZP
  - [ ] jellium vs WZP 3 down, HSE


## WZP Method vs Jellium Model

The WZP method involves promoting an electron from the valence band into the defect level, with the cell remaining neutral. Based on my understanding of the
jellium model, I believe the charged state involves a total charge in the unit cell of -1 and a doubly-occupied defect level but no hole in the valence 
bands. 

## Notes on the Calculation Choices

Alkauskas et al. used
* kinetic energy cutoff of 400 eV
* alpha = 0.31 for HSE
* 96-atom supercell, optimized at HSE level
* Gamma point

I will use the same cutoff and alpha for comparison, but I may have to start with PBE-optimized geometries because Guanzhi said that he was not able to get 
the charged-state relaxation to converge at the HSE level. I am going to try relaxing the ground state at PBE then HSE, then using the ground-state, 
HSE-level wave function to try to do HSE-level relaxation of the excited state. If I am not able to get it converged like Guanzhi, then I will go to the PBE level for the excited state.

I am not sure if they used spin-polarized calculations, but I am going to include spin polarization. I am going to do the defect calculations at the Gamma 
point because we have to set the occupations manually for the WZP method, and that requires setting the occupations for each k-point separately. This choice
should also match what Alkauskas et al. did.

## Notes on the Calculation Results

The Alkauskas-paper relaxed structure had a = 3.20 A, c = 5.19 A, and u = 0.377. Relaxing the primitive cell at the PBE level gave a = 3.20 A, c = 5.21 A, 
and u = 0.376.

In comparing equilibrium positions, always atom 17 (Ga near C) that moves the most.
