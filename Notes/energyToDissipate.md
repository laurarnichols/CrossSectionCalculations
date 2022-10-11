# Energy to Dissipate 

*Based on an email thread with Andy.*

When considering a nonradiative transition, we must consider what energy is getting dissipated into phonons. The total energy does not change in the transition; the energy just gets transformed from electronic energy to vibrational energy. The configurational-coordinate diagram below (from Alkauskas et al. 2014) illustrates this change. The actual transition occurs at the crossing point of the two parabolas, where the total energy does not change. However, the vibrational energy increases from $\Theta_m$ to $\Theta_n$, with a corresponding decrease in the electronic energy $\Delta E$. This energy $\Delta E$ is the charge transition level relative to the valence band maximum (VBM).

<img width="50%" src=https://user-images.githubusercontent.com/32521892/194400557-96b4c018-aeb7-476f-a1a9-98a6c209bf53.png>

Calculating $\Delta E$ requires the calculation of the formation energy in each charge state (whether that be done with WZP or jellium). Normally, formation energies are calculated including a chemical potential for the changed elements (in our case carbon and nitrogen). However, since the charge transition level comes from the crossing of formation energies, it is the difference in them that matters, and the chemical potentials are eliminated (as is the pristine total energy).

## Jellium

First, to review for jellium, see this [review article](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.86.253). In this paper, the formation energy of a defect $X$ in charge state $q$ is defined in Eq. (1):

$$ E^f[X^q] = E_{\text{tot}}[X^q] - E_{\text{tot}}[\text{bulk}] - \sum_i n_i \mu_i + qE_F + E_{\text{corr}}. $$

> $E_{\text{tot}}[X^q]$ is the total energy from a supercell calculation containing the defect $X$, and $E_{\text{tot}}[\text{bulk}]$ is the total energy for the perfect crystal using an equivalent supercell. The integer $n_i$ indicates the number of atoms of type $i$ (host atoms or impurity atoms) that have been added to ( $n_i > 0$ ) or removed from ( $n_i < 0$ ) the supercell to form the defect, and the $μ_i$ are the corresponding chemical potentials of these species. Chemical potentials represent the energy of the reservoirs with which atoms are being exchanged; they are discussed in detail in Sec. II.B.2. The analog of the chemical potential for “charge” is given by the chemical potential of the electrons, i.e., the Fermi energy $E_F$. $E_\text{corr}$, finally, is a correction term that accounts for finite **k**-point sampling in the case of shallow impurities, or for elastic and/or electrostatic interactions between supercells. These issues are explored in detail in Sec. III.

Later in the paper, they define in Eq. (3) the charge-state transition level, which is the Fermi-level position for which the formation energies of charge states $q_1$ and $q_2$ are equal:

$$ \varepsilon(q_1/q_2) = \frac{E^f(X^{q_1}; E_F = 0) - E^f(X^{q_2}; E_F = 0)}{q_2 - q_1}, $$

where $E^f(X^{q}; E_F = 0)$ is the formation energy of defect $X$ in charge state $q$ when the Fermi level is at the VBM ( $E_F = 0$ ). Setting the zero at the VBM is common when looking at density of states or formation-energy plots. Although we say we are setting $E_F = 0$, we are actually setting $E_F = E_{\text{VBM}}$, which is then considered zero. $E_{\text{VBM}}$, which is the energy level of the VBM in the pristine cell (can use supercell or primitive; should be the same within numerical error).

To calculate $\Delta E$, the pristine-energy and chemical-potential terms cancel, leaving

$$ \varepsilon(q_1/q_2) = \frac{E_{\text{tot}}[X^{q_1}] - E_{\text{tot}}[X^{q_2}] + (q_1 - q_2) E_{\text{VBM}} + E_{\text{corr}}(q_1) - E_{\text{corr}}(q_1)}{q_2 - q_1}. $$

$E_{\text{corr}}$ is the finite-cell calculation for jellium calculations which can be done as explained [here](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.102.016402). $E_{\text{corr}}$ only exists for charged supercells. The correction is larger for higher charge states. It also depends on the screening in the system, so two different materials with similar supercell sizes will not necessarily have the same corrections.

> **Note:** If your supercell is too small, the neutral-defect formation energy will depend on supercell size due to relaxation effects. However, if possible, your supercell should always be converged or close enough with respect to the neutral formation energy. However, when you have charged unit cells via jellium, you have electrostatic interactions between the periodic images of the charges. In general, if you keep increasing your supercell for the charged defect (even past where the neutral defect converges), you'll find that the formation energy (without the correction) will have a parabolic trend if you plot Formation energy vs 1/L where L is some length scale associated with the unit cell (for cubic cells this would just be the lattice constant).

The tool Andy usually uses to calculate $E_{\text{corr}}$ is obtainable [here](https://sxrepo.mpie.de/projects/sphinx-add-ons/files) (though others exist). 

> **Note:**  Use sxdefectalign.bz2 and its manual - DO NOT use the 2D one. This warning is based on work Xiaguang, Sok, and Andy have on the back burner. That prescription for 2D is bogus as the jellium fails severely in 2D materials, but in bulk materials it is ok-ish.

As an example, Andy ran some calculations based on input files I gave him and got $E_{\text{tot}}[X^{0}] = -730.29195$ eV and $E_{\text{tot}}[X^{-1}] = -725.08759$ eV (jellium). Note that since the jellium calculation has an even number of electrons and the defect doesn't support triplet spin states, the jellium calculation can be non-spin-polarized. The VBM in his defect-free cell is 4.242255 eV. (Sometimes you can use the valence band of the neutral defect cell if the hybridization isn't too strong.) He didn't generate the $E_{\text{corr}}$ because he would have to generate the local potential files ( `LVTOT = .FALSE.` `LVHAR = .TRUE.` ) and run that code above. For now, we'll call it 0 (though usually it is on the order of 0.1 to 0.2 depending on the supercell size, and it can be larger for higher-valued charge states). So

$$ \varepsilon(-/0) = \frac{-725.08759 + 730.29195 - 4.24244}{0 + 1} =  0.96192 \text{ eV}.$$

## WZP Method

Now, to do similarly for the WZP method. Again, there's nothing special about the $q = 0$ charge state. The formation energies in WZP are given [here](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.119.105501) in Eq. (6) for the case we care about of $q < 0$ (Eq. (5) for $q > 0$). Eq. (6) is 

$$ \tilde{E}\_q^{\text{form}}(\mu_e) = \tilde{E}\_q^{N-1} + q(\mu_e - E\_{\text{hole}} ) - \sum_i n_i \mu_i - E^N, $$

where $E^N$ is the total energy of the perfect-crystal system. Again, the defect-atom potential and total energy of the perfect crystal cancel. However, there is some ambiguity in setting $\mu_e$, which is taken to be the VBM. It is unclear whether it should be the VBM in the defect-free or the defective supercell. In the case of GaN, it differs by about 0.1 or 0.2 eV. 

Here, the total energy of the defect in the charge state is needed and then there is a difference in the energy of the Fermi energy (which we will take to be the actual valence band) and the band you took the electron from (the third down in this case though in the WZP paper they call this $E\_v$ ). Both the Fermi level (VBM) and band energy for the hole are taken from the ground-state calculation. Like before the chemical potentials will cancel. 

From Andy's calculations: $q(μ_e - E_v) = q (E_{\text{VBM}} - E_{\text{hole}}) = -1(4.403816 - 4.115236)$ and WZP $\tilde{E}\_{-1}^{N-1} = -729.15137$ eV. So we have

$$ \varepsilon(-/0) = \frac{-729.15137 - 1(4.403816 - 4.115236) + 730.29195}{0 + 1} =  0.85199 \text{ eV}.$$

