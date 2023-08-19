# Initial charge state

* Use relaxed geometry from ground-state defect as a starting point
* WZP method used to make defect positive
* Filled valence bands, empty defect state in both channels, and single carrier in CBM in spin-up channel
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Onyx  | 308 | 5 hrs | |
| Relax | PBE | Gamma | Perlmutter  | 384 | 3 hrs | |
| SCF | PBE | Gamma | Onyx | 308 | ? < 1 hr | tighter convergence and more bands |
| SCF | PBE | Gamma | Perlmutter | 384 | 10 min. | tighter convergence and more bands |
| SCF | PBE | Gamma | Narwhal | 384 | 14 min. | from scratch with `vasp_gam`, tighter convergence and more bands |
| SCF | HSE | Gamma | Onyx | 616 | ? ~14 hrs | `vasp_gam`, tighter convergence and more bands |
| Export | PBE | Gamma | Onyx | 220 | 2 min. | `-nb 4` |
| Export | HSE | Gamma | Onyx | 220 | 1 min. | energies only, `-nb 4`
