# Hydrogenated $\text{O}_{\text{N}}$ Substitutional Defect in $\text{GaN}$

We will be considering the hydrogenated oxygen substitutional defect on a nitrogen site for our first pass at the hydrogen release problem. First, I need to determine where the H prefers to sit. I set up four different H positions opposite the bonding Ga atoms. I labeled the bond directions $[-1, -1, -1]$, $[0, 0, 1]$, $[0, 1, -1]$, and $[1, -1, -1]$, based on the direction of the H relative to the O. *These planes are not right on line, but they give a clear distinction between the different positions. If we talk about them, we may want to be more precise.* For the H in the c-direction, I also set up a displaced geometry where the O is shifted as in the $DX$ center geometry seen in AlGaN. I don't expect the added H to stabilize this geometry in GaN, but I wanted to try just in case. 

| Start Geometry | Total E (eV) | O-H bond length (A) |
|------|------------|----------|
| H $[0, 0, 1]$ | -2182.45864032 | 1.00 |
| H $[0, 1, -1]$ | -2182.64179046 | 1.01 |
| H $[-1,-1,-1]$ | -2182.64336409 | 1.01 |
| H $[1,-1,-1]$ | -2182.64327529 | 1.01 |
| Disp. H $[0, 0, 1]$ | -2183.67306109 | 1.52 |
| H $[0, 0, -1]$ | -2182.68135444 | 0.99 |
| `DX_Hup` | -2183.67286721 | 1.52 |

For the non-displaced geometries, we see that there are three energy-degenerate sites across from the equivalent Ga-O bonds (the three that are slightly shorter). The position across from the Ga-O bond in the $c$-direction is higher in energy. 

In the 2004 Van de Walle review paper, however, they point out two potential positions for H depending on its charge state: in the antibonding position in the hexagonal channel (as in the three equivalent positions above) for H$^-$ or along the Ga bond in the $c$-direction. Those results were for a N atom, so I am going to test the bond-center site with the O as well (`nonDisp_00-1`).

The geometry with the H along the Ga-O in the $c$-direction is the lowest energy configuration with the O-H bond and matches the expected location of H based on previous results in GaN. 

Even though I was initially confused on how to set up the $DX$ center geometry because there were no axes given in the Puzyrev 2014 Gate paper, the displaced-oxygen configuration actually did result in the O relaxing into the $DX$ center geometry. However, the H is not bonded to the O, it is instead bonded to the Ga with the dangling bond towards the N vacancy that is left behind when the O shifts away. After talking with Sok, I want to try two configurations: one with H on the other side of O as the Puzyrev 2014 Gate paper had in AlGaN (`DX_Hdown`) and one with the H on the side that it is now but bonded to the O (`DX_Hup`). 

The geometry with the H on the side of the previous Ga bond relaxes to the same configuration with the H bonded to the Ga. 