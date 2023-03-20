# Phonons

Phonon calculations are needed to get the frequency and vector displacement of each phonon mode. The final phonons (ground state for the +/0 transition) are used as input to the rest of the capture code (the algebra assumes that the frequencies do not change in the initial and final states).

Calculations follow directions laid out in [this note](https://github.com/laurarnichols/CrossSectionCalculations/blob/main/Notes/phonons.md), except the symmetry tolerance for the 4x4x4 supercell was lowered to the default `1E-5`. Need to confirm that this is okay and figure out how to validate. 
