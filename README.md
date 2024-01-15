# Cross Section Calculations

This repo holds files needed for running calculations for the cross section project. Goals of this repo:
* Track changes in the problem to solve over time
* Track progress of various tasks needed to solve a given problem
* Transfer output files between devices for analysis
* Hold summary of results (not large output files) for long-term reference
* Keep relevant input files to ease recreating calculations in the future

## Recreating Barmparis Results and Transitioning to VASP

When I first joined the group, we were not able to recreate the results from the Barmparis paper. My first step was to figure out how the codes worked together and recreate the matrix elements from the first paper (not phonons because those were totally different). I was not able to do this in QE, and we ran into issues with doing GaN calculations in QE because we wanted to include the 3$d$ electrons in the valence. I completely rewrote the Export code to work with VASP, and I optimized and parallelized all of our codes so that we could use larger supercell sizes. With the new code, I was then able to [recreate the Barmparis matrix elements](./RecreateBarmparisMatrixElements/) using VASP. 

## Time-Domain Capture Paper

I was then supposed to look through the GaN paper because it was supposed to be done. I just needed to understand what was done to use the theory and codes for the H release problem. There were many issues that came up when I scrutinized the paper, so I rewrote a significant portion of the paper and redid the Si calculations. The details of those calculations and relevant inputs/outputs and results are given in the [TimeDomainPaper](./TimeDomainPaper/) folder. 

## Si-H Potential

We originally thought that anharmonicity was going to give us the "displacement" that would cause the zeroth-order term to be zero and the first-order term to be multiphonon. To confirm that anharmonicity would be relevant, I did a quick plot of the total energy as a function of the Si-H bond length in the SiVH3 defect that we worked with for the time-domain paper. Those results are given in the [Si-H_potential](./Si-H_potential/) folder.

## Si-SiO$\_2$ Interface

We originally thought that we would treat dehydrogenation of a dangling bond at a Si-SiO$\_2$ interface, so I [did some work](./Si-H_potential/) with a system that Blair sent. I did not get very far, though, because the system was difficult to even relax, so the calcualtions we need would be completely infeasible. Creating a new system would be possible, but setting up the amorphous silicon dioxide is not trivial.

## Defect Exploration in GaN

We then moved to considering different defects in GaN since it would be easier to work with. GaN has the added benefit that different band states could be more localized around the N atoms or Ga atoms. We decided that, because the anharmonicity does not give a real displacement, it would not be legitimate to use that displacement as the $\Delta q_j$ in our formalism. Instead, just like capture, we consider the displacement as coming from a change in the charge density with specific electronic transitions that causes a relaxation. The potential localization of the charge density on different elements in GaN could provide a large effect that would result in a relaxation. My convergence of calculations with GaN and explorations of defects in GaN are found in the [DefectExplorationInGaN](./DefectExplorationInGaN/) folder.