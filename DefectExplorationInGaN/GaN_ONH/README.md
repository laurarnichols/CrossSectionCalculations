# Hydrogenated $\text{O}_{\text{N}}$ Substitutional Defect in $\text{GaN}$

Energies of all configurations tried in order of increasing energy (details given below):

| Start Geometry | Total E (eV) | Bond length (A) |
|------|------------|----------|
| DX disp. along eig. | -2184.15514066 | not bonded |
| Disp. H $[0, 0, 1]$ | -2183.67306109 | 1.52 (Ga-H) |
| `DX_Hup` | -2183.67286721 | 1.52 (Ga-H) |
| H bond $[0, 0, -1]$ | -2182.68135444 | 0.99 (O-H) |
| H antibond $[-1,-1,-1]$ | -2182.64336409 | 1.01 (O-H) |
| H antibond $[1,-1,-1]$ | -2182.64327529 | 1.01 (O-H) |
| `DX_Hdown` | -2182.64302866 | 1.01 (O-H) |
| H antibond $[0, 1, -1]$ | -2182.64179046 | 1.01 (O-H) |
| H antibond $[0, 0, 1]$ | -2182.45864032 | 1.00 (O-H) |

Our plan was to consider the oxygen substitutional defect on a nitrogen site for the first pass at the hydrogen release problem. Before doing the scattering problem, I sought to find the most optimal geometry for the hydrogenated defect. 

I started by considering the H bonded with the O in the direction of each of the antibonding sites (labeled by the planes that the displacements approximately line up with). I also considered the position along the longest Ga-O bond (along the $c$-direction), which ended up being the configuration with the lowest energy that included the H still bonding to the O. 

There was also a lot of talk in the literature about the potential $DX$-center geometry of the O substitutional defect under certain conditions, so I wanted to also consider that geometry. I started with the geometry labeled "Disp. H" because I thought the O was displaced into the $DX$-like position with the H bonded to it. That wasn't actually correct, but displacing the O led to the system bouncing back and forth and ultimately relaxing to the actual $DX$-center configuration with the H now bonded to the Ga that the O migrated away from. 

Just to be safe, I used the actual $DX$-center configuration as the starting point and put the H on either side of the O (up/$+c$ and down/$-c$). The down position relaxed to the antibonding position, so it was not energetically favorable. The up position relaxed to the same configuration found previously with O at the $DX$ site and H bonded to the Ga left behind. This configuration is almost 1 eV lower in energy than the other configurations, so we decided to use that moving forward. 

However, once I calculated the phonons, I found a mode with a negative frequency, indicating that the configuration was unstable. I displaced the atoms along that eigenvector then re-relaxed and got a new configuration that was 0.5 eV lower in energy. This resulting geometry has H in the hexagonal channel not bonded to any of the other atoms, so it is not a straightforward use case for the H release problem. We are going to try using another defect. 