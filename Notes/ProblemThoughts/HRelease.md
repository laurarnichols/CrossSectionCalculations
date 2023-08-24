# H Release

## Algorithm design

Problem setup:
* VASP and Export
  * Pristine (_wave functions and group velocity_)
  * Defect relax and SCF (_wave functions_)

First step:
1. Define a small displacement of the H atom
2. Capture code

## Questions

### Final-state wave function
_Should the final state still be the defect wave functions or should it be the perfect-crystal wave functions?_ It seems to be like the final-state wave functions should stay the defect wave functions. My desire to make the final-state wave function also the perfect-crystal wave function comes from wanting to be consistent with the approximation of the initial-state wave function as the perfect-crystal wave function. However, the two are not treated equivalently in the algebra. The _many-body_ wave functions $|\Psi_l\rangle$ are __not__ approximated as the _many-body_ perfect-crystal wave functions. It is only the single-particle initial state $|\psi_i\rangle$ that gets approximated as the equivalent state in the perfect-crystal. However, the transition from the many-body wave functions to the single-particle wave functions happens after the transformation $$\langle \Psi_{f} | H_1^{\text{BO}} |\Psi_{i}\rangle = \langle\Phi\_f| \Psi\_i\rangle (\tilde{E}\_f - \tilde{E}\_i).$$ Transitioning there gets rid of the potential in the middle of the matrix element and allows us to exploit the orthonormality of the single-particle orbitals. After the transition to the single-particle states, we approximate the initial state as the perfect-crystal state because the carrier is considered as coming from far away from the defect. That justifies why the initial state can be approximated as the perfect-crystal state while the final state ends up as the defect final state.

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
 
