# Pristine

| Step | Choices | Processors | Time |
|------|---------|------------|------|
| Volume relax | Gamma | 220 | 22 min. |
| SCF | Gamma, tighter convergence and more bands | 220 | 9 min. |
| NSCF | 3x3x3, 'ISYM=-1`, `KPAR=3` | 660 | 2 hours and 41 minutes |
| Export | Gamma, `-nb 4` | 220 | 5 minutes |
| Export | 3x3x3, `-nk 9 -nb 4` | 396 | 5 minutes |

