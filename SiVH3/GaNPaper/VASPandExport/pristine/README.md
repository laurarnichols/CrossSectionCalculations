# Pristine

Had to keep switching betwen computers, so multiple times are shown.

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| Relax | PBE | Gamma | Onyx | 220 | 18 min. | |
| Relax | PBE | Gamma | Perlmutter | 256 | 50 min.  | |
| SCF | PBE | Gamma | Perlmutter | 256 | 6 min. | Tighter convergence and more bands |
| SCF | PBE | Gamma | Narwhal | 256 | 6 min. | Tighter convergence and more bands |
| Export | PBE | Gamma | Onyx  | 220 | 5 min. | `-nb 4` |
| Export | PBE | Gamma | Narwhal  | 256 | 1 min. | `-nb 4` |
| NSCF | PBE | 3x3x3 | Onyx | 660 | 2:41 hrs | `ISYM=-1`, `KPAR=3` |
| Export | PBE | 3x3x3 | Onyx | 396 | 5 min. | `-nk 9 -nb 4`

