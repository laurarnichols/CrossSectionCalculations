# Neutral charge state, neutral positions

* Relaxed this charge state first because it is the ground state
* Relaxation from Guanzhi's starting geometry took longer than original
* Use geometry for starting point for excited-state relaxations
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Functional | KPOINTS | Machine | Processors | Time | Notes |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Perlmutter+Narwhal | 512+384 | 6+1:34 hrs | Started on Perlmutter but then got locked out, so had to switch to Narwhal |
| SCF | PBE | Gamma | Narwhal | 384 | 11 min. | tighter convergence and more bands |
| SCF | PBE | Gamma | Narwhal | 384 | 12 min. | from scratch with `vasp_gam`, more bands |
| SCF | HSE | Gamma | Narwhal | 768 | 7:10 hrs | from PBE results, `vasp_gam`, more bands |
| Export | PBE | Gamma | Onyx | 220 | 2 min. | `-nb 4` |
| Export | HSE | Gamma | Onyx | 220 | 1 min. | energies only, `-nb 4`|
