# Neutral charge state, positive positions

* Use relaxed positions from positive charge state
* Do not relax, only SCF/NSCF

| Step | Functional | KPOINTS | Machine | Processors | Time | Notes |
|------|------------|---------|---------|------------|------|---------|
| SCF | PBE | Gamma | Perlmutter | 512 | ~6 min. | tighter convergence and more bands |
| SCF | PBE | Gamma | Narwhal | 384 | 7 min. | from scratch with `vasp_gam`, more bands |
| SCF | HSE | Gamma | Narwhal | 768 | 7:10 hrs | from PBE results, `vasp_gam`, more bands |
| Export | HSE | Gamma | Narwhal | 256 | 20 s | energies only, `-nb 4`|

## Original times

| Step | Choices | Processors | Time |
|------|---------|------------|------|
| SCF | PBE, Gamma, tighter convergence and more bands | 308 | 30 min. |
| SCF | HSE, Gamma, `vasp_gam`, tighter convergence and more bands | 616 | ? ~14 hours |
| NSCF | PBE, 3x3x3, `ISYM=-1`, `KPAR=3` | 924 | 4 hours and 4 minutes |
| Export | PBE, Gamma, `-nb 4` | 220 | 2 minutes |
| Export | HSE, Gamma, energies only, `-nb 4` | 220 | 1 minute |
| Export | PBE, 3x3x3, `-nk 9 -nb 4` | 396 | 23 minutes |

