# VASP Files

# POTCAR

_Based on emails from Andy_

Almost every supercomputer has these files available somehwere, typically somewhere like `/app/vaspapp/Potentials` with subdirectories for different versions. To access these files, you must be a member of the `vasp` group on the supercomputer. If you aren't, you can submit a ticket to the help desk to have them add you.

The newest versions of the pseudopotentials is 5.4. The difference between this version and version 5.2 on many of the supercomputers is mostly in a bunch of the ones labeled as `_GW` potentials. These potentials are needed for doing GW calculations and certain types of excited state calculations for certain elements (e.g., to have d-projectors for the conduction band of silicon for spectroscopies). For most of the normal potentials (like silicon, oxygen, etc.) they haven't changed in many many years.

## Different versions available

For some of the elements, there are `_s` and `_h` versions (primarily for the first row) - these are pseudopotentials that are softer or harder than the standard pseudopotential meaning that a smaller or larger cutoff is required. Harder pseudopotentials are sometimes needed for improved accuracy of dimers. Sometimes, softer pseudopotentials are used when working in big systems and lower cutoff energies are beneficial due to computational cost. Usually, we just use the standard one that will not have an appended letter. 

Some elements will have `_d`, `_pv`, or `_sv`. These mean that additional electrons are included from the core region as pseudo-valence. For early transition metal ions, these are often used as well as for the alkali and alkaline earth metals (e.g., for $\text{SrTiO}\_3$, you'd usually use `Sr_sv`, `Ti_pv`, and `O` pseudopotentials. For Sr there is no choice, for Ti often the plain Ti doesn't give good enough results). For Ga, this choice also exists with the `Ga` vs `Ga_d` and for some semiconductors when working with defects the extra electrons are necessary.

The `_GW` is used for doing many-body GW calculations when using that technique for improved band gaps and excited state spectroscopy calculations.

Rare earth metals sometimes have a `_2` and `_3` which relates to what oxidation state they were generated for. This is because f-electrons can be a notorious challenge in pseudopotential DFT to describe correctly so in some cases the f electrons can be set in a specific configuration and then frozen into the core.

Sometimes, you may see a `_new` which means that the pseudopotential has been regenerate at some point and usually should be used instead of the older one (unless specific compatibility is needed with old calculations).

There is a `README.UPDATES` file as well which denotes the dates when most were created and often gives information as to why one had to be regenerated. For example, sometimes pseudopotentials once tested in a wide variety of systems may be shown to have a so-called "ghost state" in which the pseudopotential produced an unphysical energy level that shouldn't exist but does for some geometry. This is also why pseudo-potential creation can sometimes be a bit of an art form and not for the faint of heart. Sometimes they'll also say if they change the file name to remove old ones. 
