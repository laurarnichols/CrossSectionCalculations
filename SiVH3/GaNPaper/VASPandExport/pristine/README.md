# Pristine

| Step | Choices | Machine | Processors | Time |
|------|---------|------------|------| -------|
| Relax | Gamma | Onyx | 220 | 18 min. |
| SCF | Gamma, tighter convergence and more bands | Perlmutter | 256 | 6 min. |
| Export | Gamma, `-nb 4` |  | 220 | 5 minutes |
| NSCF | 3x3x3, `ISYM=-1`, `KPAR=3` |  | 660 | 2 hours and 41 minutes |
| Export | 3x3x3, `-nk 9 -nb 4` |  | 396 | 5 minutes |

