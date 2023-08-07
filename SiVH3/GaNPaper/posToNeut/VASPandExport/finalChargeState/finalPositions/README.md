# Final charge state, final positions

* Relaxed this charge state first because it is the ground state
* Use geometry for starting point for excited-state relaxation
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Choices | Processors | Time |
|------|---------|------------|------|
| Relax | PBE, Gamma | 308 | 6 hours |
| SCF | PBE, Gamma, tighter convergence and more bands | 308 | ? < 1 hour |
| SCF | HSE, Gamma, `vasp_gam`, tighter convergence and more bands | 616 | ? ~14 hours |
| Export | PBE, Gamma, `-nb 4` | 220 | 2 minutes |
| Export | HSE, Gamma, energies only, `-nb 4` | 220 | 1 minute |
