# Phonons

Our capture calculations require the phonon frequencies and displacement vectors. These should be taken from the final relaxed state. The ground state can also be used as we assume that the phonons do not change between the two charge states. 

## Steps
_Adapted from email from Guanzhi_

1. Create a new folder (e.g., `Phonon`) and copy the relaxed `CONTCAR` for the system you are considering to it as `POSCAR`.
2. Change to `Phonon` folder. Make sure relaxed `POSCAR` is there. [Run](../Scripts/onyx/run_Phonopy_dispGen.scr)
```
phonopy -d --dim="1 1 1"
```
3. You will see some new files named `POSCAR-xxx`. For each, you should make a new folder `disp-xxx` in `Phonon` folder and move `POSCAR-xxx` to the folder, then do an SCF (no relaxation) in each `disp-xxx` folder. [This script](../Scripts/submitVASPBatch.scr) can be used to set up folders and submit VASP calculations.
5. After finishing all scf, [run](../Scripts/onyx/run_Phonopy_forceGen.scr) the following in Phonon folder to create `FORCE_SETS` (replace `xxx` with the max number)
```
phonopy -f disp-{001..xxx}/vasprun.xml
```
6. Check that `FORCE_SETS` has been created.
7. Prepare the following setting file (e.g., `mesh.conf`)
```
DIM = 1 1 1
MP = 1 1 1
EIGENVECTORS = .TRUE.
SYMMETRY_TOLERANCE = 1e-7
```
8. [Run](../Scripts/onyx/run_Phonopy_meshGen.scr) the following in `Phonon` folder:
```
phonopy mesh.conf
```
9. The phonon results are written into `mesh.yaml`
