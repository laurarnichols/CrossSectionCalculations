# Pristine supercell 

## Relaxation

After relaxing the [primitive cell](../primitive/) and tuning the HSE mixing parameter, I set up the pristine supercell. First, I transformed to the orthorhombic cell using a `[[1, -1, 0],[1, 1, 0], [0, 0, 1]]` transformation matrix.

To get the 96-atom supercell, I then used a 3x2x2 copy of the orthorhombic cell. 3x2x2 is chosen so that the resulting supercell is as cubic as possible. I started with the 96-atom cell because that is often used in the literature and that is what was used in the GaN paper. Using that supercell, I was getting a lower-energy defect geometry as compared to what I see in the literature, but Sok suggested that we go up a size to get more accuracy. The next-size-up, roughly-cubic supercell is 5x3x3 with 360 atoms. 

Since the primitive cell was relaxed at the HSE level and an HSE relaxation in the supercell would take a long time, I only relax at the PBE level for supercells. **The cell parameters are set by the primitive cell calculation, so further relaxations should be inner DOF only.**

## Band-decomposed charge density

We want to find states that might produce a $\Delta q$ due to a difference in the localization of the carrier. Sok said to plot the band-decomposed charge density along different lines in the supercell for bands up to 1.5 eV above the CBM. Looking at the PBE results, bands 1621-1627 are within 1.7 eV of the CBM. 

I did the plot (results in the [Analysis notebook](../../Analysis.ipynb)) and saw that all of the band states are localized on the N. Moreover, there are not any states within 1.5 eV of the CBM. I emailed Sok and Xiaoguang to see what they think the next steps should be.
