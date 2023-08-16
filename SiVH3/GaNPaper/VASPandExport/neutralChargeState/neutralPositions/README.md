# Neutral charge state, neutral positions

* Relaxed this charge state first because it is the ground state
* Use geometry for starting point for excited-state relaxations
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Onyx | 308 | 6 hrs | |
| SCF | PBE | Gamma | Onyx | 308 | ? < 1 hr | tighter convergence and more bands |
| SCF | HSE | Gamma | Onyx | 616 | ? ~14 hrs | `vasp_gam`, tighter convergence and more bands |
| Export | PBE | Gamma | Onyx | 220 | 2 min. | `-nb 4` |
| Export | HSE | Gamma | Onyx | 220 | 1 min. | energies only, `-nb 4`|
