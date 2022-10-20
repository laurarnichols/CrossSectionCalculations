# Cross Section Calculations

This repo holds files needed for running calculations for the cross section project. Goals of this repo:
* Track changes in the problem to solve over time
* Track progress of various tasks needed to solve a given problem
* Transfer output files between devices for analysis
* Hold summary of results (not large output files) for long-term reference
* Keep relevant input files to ease recreating calculations in the future

## Basic Calculations

For basic cross-section calculations, we need to do the following DFT calculations:
* Pristine supercell
   * Relax
   * SCF
   * NSCF at higher k-point density, if applicable
* Initial charge state of defect
   * Relax
   * SCF
   * NSCF at higher k-point density, if applicable
* Final charge state of defect
   * Relax (to get $\Delta q$ after capture)
   * SCF on top of initial-charge-state relaxed positions (for final wave function)
   * NSCF on top of initial-charge-state relaxed positions at higher k-point density, if applicable

We then need to run our code (details to come).

In this repo, each defect should have its own folder to hold the input files for the above calculations. Any specific problems related to these basic calculations (e.g., comparing WZP to jellium) will then refer to these base input files.
   
## Specific Problems

For each independent problem,
* A new folder should be made
* A `README.md` file should be created in that directory with
  * A description of the problem
  * A task list for calculations/analysis steps that need to be done
  * Notes on undergoing the calculations, if any
  * A summary of the results
* Input files that differ from the base files should be committed along to way to track changes
* Any analysis data like spreadsheets, plots, images, etc. should be included
