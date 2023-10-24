# Positive charge state

* Use relaxed geometry from ground-state defect as a starting point
* WZP method used to make defect positive
* Filled valence bands, empty defect state in both channels, and split carrier in CBM in each spin channel
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Perlmutter  | 384 | 3 hrs | |
| SCF | PBE | Gamma | Perlmutter | 384 | 10 min. | tighter convergence and more bands |
| SCF | PBE | Gamma | Narwhal | 384 | 14 min. | from scratch with `vasp_gam`, tighter convergence and more bands |
| SCF | HSE | Gamma | Narwhal | 768 | 10 hrs | `vasp_gam`; $E_{\text{tot}}=-3186.48260702$ |
| Export | HSE | Gamma | Warhawk | 256 | 11 s | energies only, `-nb 4` |
