# Pristine

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Onyx | 220 | 18 min. | |
| SCF | PBE | Gamma | Perlmutter | 256 | 6 min. | Tighter convergence and more bands |
| Export | PBE | Gamma | Onyx  | 220 | 5 minutes | `-nb 4` |
| NSCF | PBE | 3x3x3 | Onyx | 660 | 2 hours and 41 minutes | `ISYM=-1`, `KPAR=3` |
| Export | PBE | 3x3x3 | Onyx | 396 | 5 minutes | `-nk 9 -nb 4`

