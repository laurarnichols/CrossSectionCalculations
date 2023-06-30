# Final charge state, initial positions

* Use relaxed positions from initial charge state
* Do not relax, only SCF/NSCF

| Step | Choices | Processors | Time |
|------|---------|------------|------|
| SCF | PBE, Gamma, `ISYM=0`, tighter convergence and more bands | 308 | 30 min. |
| SCF | HSE, Gamma, `vasp_gam`, tighter convergence and more bands | 616 | ? ~14 hours |
| NSCF | PBE, 3x3x3, 'ISYM=-1`, `KPAR=3` | 924 | 4 hours and 4 minutes |
| Export | PBE, Gamma, `-nb 4` | 220 | 2 minutes |
| Export | HSE, Gamma, energies only, `-nb 4` | 220 | 1 minute |
| Export | PBE, 3x3x3, `-nk 9 -nb 4` | 396 | 23 minutes |

