# Pristine supercell 

After relaxing the [primitive cell](../primitive/) and tuning the HSE mixing parameter, I set up the pristine supercell. First, I transformed to the orthorhombic cell using a `[[1, -1, 0],[1, 1, 0], [0, 0, 1]]` transformation matrix.

To get the 96-atom supercell, I then used a 3x2x2 copy of the orthorhombic cell. 3x2x2 is chosen so that the resulting supercell is as cubic as possible. I started with the 96-atom cell because that is often used in the literature and that is what was used in the GaN paper. Using that supercell, I was getting a lower-energy defect geometry as compared to what I see in the literature, but Sok suggested that we go up a size to get more accuracy. The next-size-up, roughly-cubic supercell is 5x3x3 with 360 atoms. 

Since the primitive cell was relaxed at the HSE level and an HSE relaxation in the supercell would take a long time, I only relax at the PBE level for supercells. **The cell parameters are set by the primitive cell calculation, so further relaxations should be inner DOF only.**

Not sure what wave functions we are or aren't going to need and/or what bands we want to look at, so I only did the relaxation for now. Will need to copy the `CONTCAR` to the `POSCAR` and run an SCF calculation with more bands and a tighter convergence if we need the wave functions.
