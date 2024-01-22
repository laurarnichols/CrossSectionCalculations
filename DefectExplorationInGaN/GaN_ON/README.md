# $\text{GaN}$ with $\text{O}_{\text{N}}$ Substitutional Defect

We chose this defect because of its low formation energy and the ability to compare with experiment. 

First, to set up the defect, I picked a N atom (248) near the center of the cell at $(0.40000, 0.55556, 0.45865)$ to replace with an O atom. The pristine supercell has 
* Total energy: `-2184.16494905`
* Nearest neighbors: `158 1.94 113 1.94 104 1.94  67 1.95`

To start, I shifted the position of that atom by $(0.0, -0.1, 0.1)$ before relaxing. With that small shift, the O goes back to the original substitutional site, but the bond length to the Ga atoms has increased by 5%, which lines up with what is observed in the literature. 
* Total energy: `-2182.25614162`
* Nearest neighbors: `104 2.03 113 2.03 158 2.03  67 2.04`

I tried to calculate the formation energy to compare with experimental numbers, but I could not get numbers to match up with the literature results. However, the geometry I got matches up with the literature, so we think the issue may be in how I was calculating the chemical potentials. But we are not really worried about the formation energy, so we decided to move on.
