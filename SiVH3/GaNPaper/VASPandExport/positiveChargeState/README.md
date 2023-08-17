# Initial charge state

* Use relaxed geometry from ground-state defect as a starting point
* WZP method used to make defect positive
* Filled valence bands, empty defect state in both channels, and single carrier in CBM in spin-up channel
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Onyx  | 308 | 5 hours | |
| Relax | PBE | Gamma | Perlmutter  | 384 | ? < 6 hours | |
| SCF | PBE | Gamma | Onyx | 308 | ? < 1 hour | tighter convergence and more bands |
| SCF | HSE | Gamma | Onyx | 616 | ? ~14 hours | `vasp_gam`, tighter convergence and more bands |
| Export | PBE | Gamma | Onyx | 220 | 2 minutes | `-nb 4` |
| Export | HSE | Gamma | Onyx | 220 | 1 minute | energies only, `-nb 4`
