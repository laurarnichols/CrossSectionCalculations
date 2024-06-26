# Hybrid Theory and Calculations

## Theory
* Hybrid functionals are functionals that mix in various portions of the exact (Hartree-Fock) exchange with the exchange-correlation of other functionals (often LDA or GGA)
* The idea is that hybrid functionals can better describe properties like the band gap
* Some of the most common ones are B3LYP (chemistry) and HSE (solid state); PBE0 is also used in solid state, but most people now favor HSE
* HSE takes the form

$$ E_{\text{xc}}^{\omega \text{PBEh}} = a E_{\text{x}}^{\text{HF,SR}}(\omega) + (1 - a) E_{\text{x}}^{\text{PBE,SR}}(\omega) + E_{\text{x}}^{\text{PBE,LR}}(\omega) + E_{\text{c}}^{\text{PBE}}, $$

where $\omega$ is a screening length and $a$ is the mixing amount.
* This says that, at some short range, we’ll mix the HF exchange and the PBE exchange, keeping the PBE exchange outside the screening length, and we will always use the correlation energy from the PBE functional
* In general, the HSE functional gives reasonable band gaps for a wide range of materials
* Standard reference values are $a = 0.25$ and $\omega = 0.2$. 
* Tuning the functional is changing the $a$ parameter

### Relaxation Geometry vs PBE

*Based on email thread from Andy*

There are cases where the PBE relaxation and the HSE relaxation of a defect may end up being very different. This usually occurs if the level is shallow and is localized in HSE but not in LDA/PBE. A notable example is that of [the oxygen vacancy](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.86.155105) in $\text{SrTiO}_3$. In $\text{SrTiO}_3$, the O vacancy occurs between two Ti atoms in the lattice. At the LDA level, relaxation of the neutral vacancy occurs such that the two Ti atoms move away from each other; whereas, at the HSE level, the two Ti atoms move towards each other. The issue arises from the fact that a neutral O vacancy has 2 extra electrons that either can go into a localized level (HSE) or get dumped in the conduction band (LDA/PBE). There are ways around this by using a Hubbard U in materials that have d orbitals (though the Physics is iffy) or by using a special **k** point that artificially opens the gap for the LDA/PBE calculation. I have done the latter before in the days of not having the computational power to relax at the HSE level - so I relaxed with a special kpoint on the PBE level and then ran a single HSE calculation.

The other case that you may need to start with a completely different starting geometry is in defects that break symmetry or reconfigure. The reconfigure case can occur for so-called DX centers in wide-band-gap materials. They may even have a barrier between configurations. Also, the DFT codes usually will not spontaneously break symmetry during relaxation. For example, in GaAs, if I replace an As atom with an O atom, since the material is cubic and the atom has tetrahedral symmetry, it will stay that way with local shifting of equivalent amounts in all 4 bonds. This is correct in the neutral charge state. However, if the OAs is in the negative charge state and pushed off center, the O atom will relax into the backbone and lower the energy. Similar effects occur for the simple vacancies in silicon, diamond, and cubic III-V semiconductors. For certain charge states, the defect will remain in the Td (tetrahedral) configuration, but in others there may be distortions leading to a tetragonal symmetry breaking.

It may seem daunting that these sorts of distortions will occur, but they occur due to so-called Jahn-Teller effects. If you look at the electronic structure of the defect, you may notice that there are partially filled degenerate midgap levels. The symmetry breaking occurs to break this degeneracy. So, in the Si vacancy, when the defect is neutral, there are three mid gap levels in each spin channel and if the Td symmetry is kept, there will be two parallel spin electrons in one spin channel (so it is an $S = 1$ defect). However, allowing the symmetry to break with a tetragonal distortion will lead to the degeneracy breaking and the two electrons pairing up. So, any time you see the degeneracy you may consider a distortion (there are of course special cases like dynamical JT effects where the barrier to reconfigure between different distortions of the defect are small and the defect will actually fluctuate between all directions of distortion and lead to an averaging effect, but don't worry too much about this for now.)

## Calculations

For VASP:
* Set `LHFCALC = .TRUE.` to turn on HSE
* Recommended algorithm is `ALGO = Damped` with `TIME = 0.5`, decreasing the time step TIME if convergence is not reached 
* `Damped` and `All` are supported; `Normal` is okay but slow and has caveats; other algorithms are not supported
* `GGA = PE` for PBE functional (should come from POTCAR file, but good to specify)
* Must specify `HFSCREEN` to go from PBE0 (default, `HFSCREEN = 0`) to either HSE06 (used by Alkauskas; `HFSCREEN = 0.2`) or HSE03 (`HFSCREEN = 0.3`)
* `AEXX` is exact-exchange mixing parameter to be tuned
* When running hybrid calculations, good to have a preconverged PBE wave function/charge density to read in for faster/better convergence
