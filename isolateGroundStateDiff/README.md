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
- [x] HSE
  - [x] `LDIAG=.TRUE.`
  - [x] `LDIAG=.FALSE.`

## Results

Did not see any difference with `ISMEAR` or `LDIAG` choice at either level. Guanzhi came back and said that the difference he saw was in going from either
`ISMEAR=-2`/PBE or `ISMEAR=0`/HSE to WZP VBM HSE. Andy said that he didn't trust the `LDIAG` tag and we should avoid it if possible. 

PBE level with my base settings, comparing choice of `ISMEAR`:
![image](https://user-images.githubusercontent.com/32521892/194382932-e162790b-693b-47fb-ad7a-ea2b32a91ee3.png)

PBE level with settings Guanzhi used, comparing choice of `ISMEAR`:
![image](https://user-images.githubusercontent.com/32521892/194383168-f6bb9bf8-dfe0-4951-8055-27b2e83150cb.png)

PBE level with `ISMEAR = -2`, comparing my base tags to Guanzhi's:
![image](https://user-images.githubusercontent.com/32521892/194383317-664aed76-bc0d-4a9b-b75d-e452ee444e2d.png)

HSE level with Guanzhi's tags, comparing choice of `LDIAG`:
![image](https://user-images.githubusercontent.com/32521892/194383428-9f4c9624-86f7-4022-85ee-b35685cd71b6.png)
