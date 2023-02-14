# Phonons

Phonon calculations are needed to get the frequency and vector displacement of each phonon mode. The final phonons (ground state for the +/0 transition) are used as input to the rest of the capture code. However, the algebra assumes that the frequencies do not change in the initial and final states, so I am going to do the initial (excited-state) phonons as well to confirm that assumption.

Both calculations follow directions laid out in [this note](https://github.com/laurarnichols/CrossSectionCalculations/blob/main/Notes/phonons.md)
