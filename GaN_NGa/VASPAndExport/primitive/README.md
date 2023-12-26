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
