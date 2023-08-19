# Neutral charge state, neutral positions

* Relaxed this charge state first because it is the ground state
* Relaxation from Guanzhi's starting geometry took longer than original
* Started on Perlmutter but then got locked out, so had to switch to Narwhal
* Use geometry for starting point for excited-state relaxations
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Onyx | 308 | 6 hrs | |
| Relax | PBE | Gamma | Perlmutter+Narwhal | 512+384 | 6+1:34 hrs | |
| SCF | PBE | Gamma | Onyx | 308 | ? < 1 hr | tighter convergence and more bands |
| SCF | PBE | Gamma | Narwhal | 384 | 11 min. | tighter convergence and more bands |
| SCF | PBE | Gamma | Warhawk | 384 | 12 min. | from scratch with `vasp_gam`, more bands |
| SCF | HSE | Gamma | Onyx | 616 | ? ~14 hrs | `vasp_gam`, tighter convergence and more bands |
| Export | PBE | Gamma | Onyx | 220 | 2 min. | `-nb 4` |
| Export | HSE | Gamma | Onyx | 220 | 1 min. | energies only, `-nb 4`|
