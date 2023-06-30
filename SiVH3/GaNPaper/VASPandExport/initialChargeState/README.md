# Initial charge state

* Use relaxed geometry from ground-state defect as a starting point
* WZP method used to make defect positive
* Filled valence bands, empty defect state in both channels, and single carrier in CBM in spin-up channel
* Didn't need NSCF with 3x3x3 because don't need these wave functions

| Step | Choices | Processors | Time |
|------|---------|------------|------|
| Relax | PBE, Gamma, | 308 | 5 hours |
| SCF | PBE, Gamma, tighter convergence and more bands | 308 | ? < 1 hour |
| SCF | HSE, Gamma, , `vasp_gam`, tighter convergence and more bands | 616 | ? ~14 hours |
| Export | PBE, Gamma, `-nb 4` | 220 | 2 minutes |
| Export | HSE, Gamma, energies only, `-nb 4` | 220 | 1 minute |
