# Isolate Ground State Difference

Guanzhi did two calculations at the ground state (HSE level) with the intent to compare different choices for `ISMEAR` and got different results. However, 
his calculations not only included a change in `ISMEAR` (`ISMEAR=0`/`SIGMA=0.03` vs `ISMEAR=-2`), but they also included a change in `LDIAG` (`.TRUE.` vs 
`.FALSE.`). Xiaoguang also said that the difference could be an issue with the k-point grid not being converged, although Andy said Gamma should be
fine for our supercell size. 

To figure out what the difference is, I am going to compare the `ISMEAR` choices at the PBE level in the ground state on top of the PBE-relaxed, 
excited-state structure. If those are the same, I will then reproduce Guanzhi's HSE calculations and compare different choices of `LDIAG`. If the different 
`ISMEAR` choices aren't the same at the PBE level, I will increase the k-point grid density until I can get the results to match.

Based on the input file that Guanzhi sent (`INCAR_Guanzhi`), he was doing an SCF calculation at the HSE level on top of the PBE-optimized geometry. I will
use `ISMEAR=0` to compare the effect of `LDIAG` at the HSE level.

## Tasks

- [x] PBE
  - [x] `ISMEAR=-2`
  - [x] `ISMEAR=0`, `SIGMA=0.03`
- [ ] HSE
  - [ ] `LDIAG=.TRUE.`
  - [ ] `LDIAG=.FALSE.`

## PBE Results

Some difference between the choices of `ISMEAR`, but they aren't significant.

<table>
<tr><th></th><th>'ISMEAR=0'</th><th>`ISMEAR=-2`</th><th>Diff</th></tr>
<tr><th>E</th><td>578.0435</td><td>-578.044</td><td>-0.00057</td></tr>
<tr>
<td>

| Band |
| ---- |
| 425  |
| 426  |
| 427  |
| 428  |
| 429  |
| 430  |
| 431  |
| 432  |
| 433  |

</td>
<td>

| E up   | Occ up | E down | Occ down |
| ------ | ------ | ------ | -------- |
| 4.7298 | 1      | 4.7528 | 1        |
| 4.7466 | 1      | 4.7673 | 1        |
| 4.7865 | 1      | 4.8139 | 1        |
| 4.9138 | 1      | 4.9868 | 1        |
| 4.9867 | 1      | 5.0565 | 1        |
| 5.3208 | 1      | 5.3444 | 1        |
| 5.3550 | 1      | 5.4690 | 0.54675  |
| 5.3589 | 1      | 5.4739 | 0.45325  |
| 7.1379 | 0      | 7.1495 | 0        |

</td>
<td>

| E up   | Occ up | E down | Occ down |
| ------ | ------ | ------ | -------- |
| 4.7328 | 1      | 4.7484 | 1        |
| 4.7452 | 1      | 4.7603 | 1        |
| 4.7828 | 1      | 4.8108 | 1        |
| 4.8894 | 1      | 4.9927 | 1        |
| 5.0148 | 1      | 5.0531 | 1        |
| 5.3249 | 1      | 5.3489 | 1        |
| 5.3281 | 1      | 5.4771 | 1        |
| 5.4034 | 1      | 5.4786 | 0        |
| 7.1376 | 0      | 7.1492 | 0        |

</td>
<td>

| E up     | E down   |
| -------- | -------- |
| 0.003    | \-0.0044 |
| \-0.0014 | \-0.007  |
| \-0.0037 | \-0.0031 |
| \-0.0244 | 0.0059   |
| 0.0281   | \-0.0034 |
| 0.0041   | 0.0045   |
| \-0.0269 | 0.0081   |
| 0.0445   | 0.0047   |
| \-0.0003 | \-0.0003 |

</td>
</tr> </table>
