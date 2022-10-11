# Hybrid Theory and Calculations

## Theory
* Hybrid functionals are functionals that mix in various portions of the exact (Hartree-Fock) exchange with the exchange-correlation of other functionals (often LDA or GGA)
* The idea is that hybrid functionals can better describe properties like the band gap
* Some of the most common ones are B3LYP (chemistry) and HSE (solid state); PBE0 is also used in solid state, but most people now favor HSE
* HSE takes the form

$$ E_{\text{xc}}^{\omega \text{PBEh}} = a E_{\text{x}}^{\text{HF,SR}}(\omega) + (1 - a) E_{\text{x}}^{\text{PBE,SR}}(\omega) + E_{\text{x}}^{\text{PBE,LR}}(\omega) + E_{\text{c}}^{\text{PBE}}, $$

where $\omega$ is a screening length and $a$ is the mixing amount.
* This says that, at some short range, we’ll mix the HF exchange and the PBE exchange, keeping the PBE exchange outside the screening length, and we will always use the correlation energy from the PBE functional
* In general, the HSE functional gives reasonable band gaps for a wide range of materials
* Standard reference values are $a = 0.25$ and $\omega = 0.2$. 
* Tuning the functional is changing the $a$ parameter
