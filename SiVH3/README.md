# Triply-hydrogenated Si vacancy

This folder contains subdirectories that contain details and input files to perform specific sets of calculations. The details for each calculation are given in `README.md` files throughout the folders. 

## [Recreate Paper Numbers](./recreatePaperNumbers)

The Barmparis paper used QE for all of the DFT calculations. However, VASP is faster and more versatile, so we switched to using VASP. In order to do that, we needed to update the `Export` code and transform all of the output from VASP into the form previously used by QE (what is expected by the matrix element code `TME`). In order to make sure that our new `Export` code was correct, I recreated the Barmparis paper numbers. 

## [Si-H Potential](./Si-H_potential)

To get an idea of the potential between one of the H atoms and the Si it is bonded to in the triply-hydrogenated Si vacancy, I calculated the total energy of the SiVH3 system at various positions of one of the H atoms. The goal of this was to consider how quickly (in distance and vibrational quanta) the energy gets anharmonic in order to get an idea of if anharmonic effects might be important when considering H release from inelastic scattering.

## [GaN Paper](./GaNPaper)

In the GaN paper, the phonon integration method was updated from using Monte Carlo sampling of the phonon combinations to using all possible phonon combinations through a time-domain-integration formalism. In the paper, we do the triply-hydrogenated Si vacancy again, as well as a carbon substitutional defect in Si. This folder contains the +/0 transition in SiVH3. 

In talking through the choices for the calculation, we realized that some of the choices made in the Barmparis paper were incorrect or needed to be improved on. These results will not necessarily match those in the Barmparis paper, but the defect is the same. 
