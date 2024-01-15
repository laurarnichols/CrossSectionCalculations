# Defect Exploration in GaN

First, I converged the perfect-crystal GaN calculations, first in the [primitive cell](./GaN/primitive/), then in the [pristine supercell](./GaN/pristine/). I then set up a N antisite defect because Sok thought that would be the easiest defect to work with. 

## GaN with N antisite

The files for my calculations with the N antisite defect are in the [GaN_NGa](./GaN_NGa/) folder. I had to do multiple relaxations with that defect because I was getting a geometry with a slightly lower energy than the one in the literature. I calculated the formation energy of the N antisite defect in the [Analysis](./Analysis.ipynb) notebook. 

I brought up with the group, however, that the formation of the antisite is very large--so much so that many papers do not consider it in detail. This is an issue because we want to be able to compare with experiment, not just do a toy problem. I proposed a few other alternatives and we landed on the O substitutional defect on a N site as the formation energy is low and there is threshold-voltage-shift data attributed to that defect.


