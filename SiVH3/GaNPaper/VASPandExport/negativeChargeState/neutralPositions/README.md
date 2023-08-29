# Negative charge state, neutral positions

| Step | Functional | KPOINTS | Machine | Processors | Time | Choices |
|------|------------|---------|---------|------------|------|---------|
| SCF | PBE | Gamma | Warhawk | 384 | 1 hr | tighter convergence and more bands |
| SCF | PBE | Gamma | Narwhal | 384 | 17 min. | from scratch with `vasp_gam`, more bands |
| SCF | HSE | Gamma | Narwhal | 1280 | 3:15 hrs | from Guanzhi's converged wave functions, `vasp_gam`, more bands |
| Export | PBE | Gamma | Warhawk | 256 | 1 min. | `-nb 4` |

