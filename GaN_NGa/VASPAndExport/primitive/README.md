# Primitive relaxation

* First step in setting up the supercell is volume relaxing the primitive unit cell.
* Based on parameters from Andy from working with GaN before, I used a 5x5x3 k-point mesh to relax.
* Ran PBE on 128 processors on Perlmutter and finished in 30 seconds.
* Started with `AEXX=0.31` because that is what Guanzhi and Alkauskas et al. used. After relaxation, the band gap (calculated at $\Gamma$) is 3.78 eV
* Alkauskas et al. [cite the T=0 band gap of GaN](https://pubs.aip.org/aip/apl/article-abstract/87/24/242104/905759/Temperature-and-compositional-dependence-of-the?redirectedFrom=fulltext) as 3.5 eV.
* Using `AEXX=0.29` gave a band gap of 3.65 eV
* Realized that the energy cutoff used at 400 eV is the default from the POTCARs and does not seem high enough.
* I am now planning to converge the lattice parameters in the PBE calculation with respect to energy cutoff, then switch to using HSE with the converged cutoff.

Lattice parameters are determined based on diagram below:
<p align="center">
  <img src="The-Wurtzite-structure-of-GaN.png" width="50%">
</p>

Here are the results for volume relaxing at the PBE level:
| `ENCUT` | Total E (eV) | Band Gap | a | c | u |
|------|------------|---------|---------|------------|------|
| 400 | -24.29584864 | 1.819593 | 3.20032 | 5.20969 | 1.96334 |
| 520 | -24.30076274 | 1.714369 | 3.21896 | 5.24045 | 1.97545 |
| 600 | -24.30368614 | 1.714394 | 3.21896 | 5.24045 | 1.97545 |
| 650 | -24.30747166 | 1.715079 | 3.21896 | 5.24045 | 1.97545 |

Based on those numbers, I would consider the energy cutoff converged at 520 eV. Now going to use this higher cutoff to tune the band gap with HSE.