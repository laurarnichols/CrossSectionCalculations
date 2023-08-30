# H Release

## Algorithm design 1 (simplest/fastest)

This algorithm design gives the simplest approach to calculating the H release problem. We can figure out what approximations we might want to refine later.

### Problem setup
* VASP and Export
  * Pristine (_wave functions and group velocity_)
  * Defect relax and SCF (_wave functions and eigenvalues_)
  * Total energy as a function of H position
* Determine when H is "released" and step size to get there (__figure out how we will determine when the H is released__)
* Energy Tabulator: include the total energy as a function of H position 
* Phonons from relaxed initial state
* PhononPP: project initial displacement-step vector on the phonon modes and get shifted positions 
* First-order matrix element calculation
* Determine the threshold of atomic displacement for self-consistency

### Algorithm 

Repeat until the non-hydrogen atomic movements are self-consistent:
1. PhononPP: project displacement vector on the phonon modes to get $\Delta q_j$  
2. Zeroth- and first-order LSF to get energy transfer rate (__need to add energy difference to sum__)
3. Integrate over initial energy with carrier density to get total energy transfer rate (__need to confirm units are correct and figure out where the integration stops__)
$$\frac{dE}{dt} = \Omega \int n(E_i) P(E_i) dE$$
4. Use $S_j$ as a weight to split $dE/dt$ across modes to get $dE_j/dt$
5. Use a map of $E_j$ vs $\Delta q_j$ to convert to $d(\Delta q_j)/dt$ (__need to figure out where/how to get this map__)
6. Convert to $d (\Delta \mathbf{R})/dt$ using
$$d (\Delta \mathbf{Q})/dt = \sum_j [d(\Delta q_j)/dt] \hat{e}_j,$$
where $\hat{e}_j$ are the phonon eigenvectors, then
$$d (\Delta \mathbf{R}\_{ik})/dt = \frac{1}{\sqrt{m_k}} d (\Delta \mathbf{Q}\_{ik})/dt,$$
where $i$ is the x,y,z index and $k$ is the atom index.
8. Scale $d (\Delta \mathbf{R})/dt$ to match the initial set displacement of the hydrogen (other atoms will now be displaced)

Once self-consistency is achieved, capture the following values from the last loop:
1. Use the relationship $E_j = \bar{n}_j \hbar \omega_j$ to convert to $d\bar{n}_j/dt$
2. Increment the total time by the scale ($\Delta t$) used to match $d (\Delta \mathbf{R})/dt$ to the H displacement
3. Increment the $\bar{n_j}$ for each mode by $(d\bar{n}_j/dt)(\Delta t)$
4. Update the positions based on the last step
5. Test if the H was released
6. If it was, end and report $\Delta t_{\text{total}}$. If it wasn't, step the H out by another displacement step and start the loop over.
  
### Assumptions
* The energy of the system as the H migrates away is not significantly impacted by the additional atom movements
* The band eigenvalues do not significantly change as the H is displaced
* Matrix elements do not significantly change as the H migrates away
* Phonons do not change significantly
* Energy goes into phonon modes weighted by the Huang-Rhys factor

## Improvements on assumptions

### Total energy
One of the assumptions in the simple model is to move the H atom away from equilibrium towards being released to map the total energy along the path. The total energy is needed to go into the delta function for energy conservation. This delta function is highly sensitive, so one way to increase the accuracy of our calculations would be to instead recalculate the energy along the way. Here are some options in order of increasing accuracy:
1. Use the total energy curve from only moving the hydrogen from equilibrium to release
2. Use the total energy curve from only moving the hydrogen, but only do it $n$ steps at a time, with the starting point including some shifts from other atoms each time
3. Recalculate the total energy each time step only after self-consistency is reached
4. Recalculate the total energy of the system at the end of each round of the self-consistent loop to feed into the next loop

### Band eigenvalues
A related issue to the total energies would be the band eigenvalues. It would be faster to do the total energy calculations with only the default number of bands; however, adding more bands would allow also updating the eigenvalues. Each of the steps listed above (besides the first) can be seen as two steps: including the default number of bands and using the eigenvalues from the previous step or including enough bands to update all of the needed eigenvalues.

### Matrix elements
For the zeroth-order, the matrix elements are relatively cheap if all of the bands are included. The VASP calculations would need a tighter convergence, and the TME code would need to be run again. The recalculation could be done at any of the frequencies given in the total energy section. For the first-order, however, the matrix elements would very expensive to do any more than 1-3 times per calculation if using a large supercell. This should only be considered if there are significant accuracy issues introduced by using fixed matrix elements.

### Phonons
The phonons are also relatively expensive (though not as expensive as the first-order matrix elements). Similar to the first-order matrix elements, only recalculate the phonons if significant errors are introduced. If the phonons are recalculated, the first-order matrix elements should be recalculated as well. 

### Energy split up by Huang-Rhys factor
The choice of using the Huang-Rhys factor as a weight to split the energy into all of the modes, while well-motivated in the theory, is somewhat arbitrary. It guarantees that the modes most-coupled to the movement of the hydrogen dominate, which is the main effect that we wanted to capture.

Another potential idea is splitting up the total energy-transfer rate by $P_j$, which comes from running the LSF code with a single mode enabled.

## Questions

### Final-state wave function
_Should the final state still be the defect wave functions or should it be the perfect-crystal wave functions?_ It seems to be like the final-state wave functions should stay the defect wave functions. My desire to make the final-state wave function also the perfect-crystal wave function comes from wanting to be consistent with the approximation of the initial-state wave function as the perfect-crystal wave function. However, the two are not treated equivalently in the algebra. The _many-body_ wave functions $|\Psi_l\rangle$ are __not__ approximated as the _many-body_ perfect-crystal wave functions. It is only the single-particle initial state $|\psi_i\rangle$ that gets approximated as the equivalent state in the perfect-crystal. However, the transition from the many-body wave functions to the single-particle wave functions happens after the transformation $$\langle \Psi_{f} | H_1^{\text{BO}} |\Psi_{i}\rangle = \langle\Phi\_f| \Psi\_i\rangle (\tilde{E}\_f - \tilde{E}\_i).$$ Transitioning there gets rid of the potential in the middle of the matrix element and allows us to exploit the orthonormality of the single-particle orbitals. After the transition to the single-particle states, we approximate the initial state as the perfect-crystal state because the carrier is considered as coming from far away from the defect. That justifies why the initial state can be approximated as the perfect-crystal state while the final state ends up as the defect final state.

### Code design
_What is the best way to set up this code? Should I just use a bash script to run each of the individual pieces? Or should I try to figure out a way to get everything I need from each part of the program by a subroutine call?_ Could update the codes so that a single subroutine is called to get the information needed from that code. In the actual program, the main program would get input from the user, call the main subroutine, then handle writing the information out to files. In the scattering code, the subroutines could then be called to get the required information without writing new files out at every step. This would also avoid having to submit multiple jobs, which would limit total queue time.
 
