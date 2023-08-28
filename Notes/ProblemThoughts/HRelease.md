# H Release

## Algorithm design 1 (simplest/fastest)

This algorithm design gives the simplest approach to calculating the H release problem. We can figure out what approximations we might want to refine later.

### Problem Setup
* Determine when H is "released" and step size to get there (__figure out how we will determine when the H is released__)
* VASP and Export
  * Pristine (_wave functions and group velocity_)
  * Defect relax and SCF (_wave functions and eigenvalues_)
  * Total energy as a function of H position
* Energy Tabulator: include the total energy as a function of H position
* Phonons from relaxed initial state
* PhononPP: project initial displacement-step vector on the phonon modes and get shifted positions 
* First-order matrix element calculation

### Algorithm 

Repeat until the non-hydrogen atomic movements are self-consistent:
1. PhononPP: project displacement vector on the phonon modes to get $\Delta q_j$  
2. Zeroth- and first-order LSF to get energy transfer rate (__need to add energy difference to sum__)
3. Integrate over initial energy with carrier density to get total energy transfer rate (__need to confirm units are correct and figure out where the integration stops__)
$$\frac{dE}{dt} = \Omega \int n(E_i) P(E_i) dE$$
4. Use $S_j$ as a weight to split $dE/dt$ across modes to get $dE_j/dt$
5. Use a map of $E_j$ vs $\Delta q_j$ to convert to $d(\Delta q_j)/dt$ (__need to figure out where/how to get this map__)
6. Convert to $d (\Delta \mathbf{R})/dt$ using
$$d (\Delta \mathbf{R})/dt = \sum_j (\Delta q_j)\hat{e}_j,$$
where $\hat{e}_j$ are the phonon eigenvectors
7. Scale $d (\Delta \mathbf{R})/dt$ to match the initial set displacement of the hydrogen (other atoms will now be displaced)

Once self-consistency is achieved, capture the following values from the last loop:
1. Use the relationship $E_j = \bar{n}_j \hbar \omega_j$ to convert to $d\bar{n}_j/dt$
2. Increment the total time by the scale ($\Delta t$) used to match $d (\Delta \mathbf{R})/dt$ to the H displacement
3. Increment the $\bar{n_j}$ for each mode by $(d\bar{n}_j/dt)(\Delta t)$
4. Update the positions based on the last step
5. Test if the H was released
6. If it was, end and report $\Delta t_{\text{total}}$. If it wasn't, step the H out by another displacement step and start the loop over.
  
### Assumptions
* Matrix elements do not significantly change as the H migrates away
* Phonons do not change significantly
* Energy goes into phonon modes weighted by the Huang-Rhys factor

## Questions

### Final-state wave function
_Should the final state still be the defect wave functions or should it be the perfect-crystal wave functions?_ It seems to be like the final-state wave functions should stay the defect wave functions. My desire to make the final-state wave function also the perfect-crystal wave function comes from wanting to be consistent with the approximation of the initial-state wave function as the perfect-crystal wave function. However, the two are not treated equivalently in the algebra. The _many-body_ wave functions $|\Psi_l\rangle$ are __not__ approximated as the _many-body_ perfect-crystal wave functions. It is only the single-particle initial state $|\psi_i\rangle$ that gets approximated as the equivalent state in the perfect-crystal. However, the transition from the many-body wave functions to the single-particle wave functions happens after the transformation $$\langle \Psi_{f} | H_1^{\text{BO}} |\Psi_{i}\rangle = \langle\Phi\_f| \Psi\_i\rangle (\tilde{E}\_f - \tilde{E}\_i).$$ Transitioning there gets rid of the potential in the middle of the matrix element and allows us to exploit the orthonormality of the single-particle orbitals. After the transition to the single-particle states, we approximate the initial state as the perfect-crystal state because the carrier is considered as coming from far away from the defect. That justifies why the initial state can be approximated as the perfect-crystal state while the final state ends up as the defect final state.

### Code design
_What is the best way to set up this code? Should I just use a bash script to run each of the individual pieces? Or should I try to figure out a way to get everything I need from each part of the program by a subroutine call?_

## Random thoughts
* Need $\Delta q$ for multiphonon. Can it just be a relaxation of the H stretch mode and/or other dominant defect modes?
* Could take the route of calculating $\Delta q$ from anharmonicity, but we have tried that route and it is very complicated.
* Could instead make a map of how much energy the H takes in to how much it will relax. 
* Two possible $\Delta q$'s: minimum to minimum if it gets over the barrier or new average position if excited anharmonic.
* How can we get the anharmonic map?
  * Ignore hits that do not give enough energy to go anharmonic
  * Move H manually to plot energy profile/barrier
  * Get H-mode quanta size from phonons
  * Map each quanta absorption to new max/min positions and a new expectation value of the position 
  * Treat the phonons as original parabola but centered at the new expectation value (Is this valid? May be needed at least as a first approximation.)
 
