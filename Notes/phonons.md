# Phonons

Our capture calculations require the phonon frequencies and displacement vectors. These should be taken from the final relaxed state. 

## Steps
_Based on email from Guanzhi_

1. Do a Gamma-only relaxation calculation on the defect in the final charge state.
2. Create a new folder (e.g., `Phonon`) and copy the relaxed `CONTCAR` to it as `POSCAR`.
3. Change to `Phonon` folder. Make sure relaxed `POSCAR` is there. Run
```
phonopy -d --dim="1 1 1"
```
4. You will see some new files named `POSCAR-xxx`. For each, you should make a new folder `disp-xxx` in `Phonon` folder and move `POSCAR-xxx` to the folder. 
5. Do an SCF (no relaxation) in each `disp-xxx` folder. 
7. After finishing all scf, run the following in Phonon folder to create FORCE_SETS (replace `xxx` with the max number)
```
phonopy -f disp-{001..xxx}/vasprun.xml
```
8. Check that `FORCE_SETS` has been created.
9. Prepare the following setting file (e.g., `mesh.conf`)
```
DIM = 1 1 1
MP = 1 1 1
EIGENVECTORS = .TRUE.
SYMMETRY_TOLERANCE = 1e-7
```
10. Run the following in `Phonon` folder:
```
phonopy mesh.conf
```
11. The phonon results are written into `mesh.yaml`
