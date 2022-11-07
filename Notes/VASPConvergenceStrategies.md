# VASP Convergence Strategies

## Parameter Convergence

* Start with a reasonable geometry (may need to preconverge with a reasonable guess of parameters if you expect a large relaxation)
* Choose reasonable starting points for all parameters
  * `PREC` -- should be at least `Normal`
  * `EDIFF` -- `1E-5` is usually okay to start 
  * `KPOINTS` -- good rule of thumb is 30-40  times reciprocal lattice parameter (e.g., if a=3, b=4, c=6, then KPOINTS be 40/a, 40/b, 40/c)
  * `ENCUT` -- use at least 1.3 times largest `ENMAX` value in `POTCAR` files
* Check if spin polarization is needed by doing a relaxation with different settings of `ISPIN` (all others constant) and seeing if the total energy changes. If the energy is the same, use non-spin-polarized calculations.
* Converge `KPOINTS`
* Other settings to (potentially) converge (static calculations except `EDIFFG`) -- _Convergence test shouldn't depend on the geometry; it should tell you how the energy converges on that potential surface_
  * `ENCUT`
  * `EDIFF`
  * `EDIFFG`
  * `NBANDS`
  * `NEDOS` for DOS calculations

Additional resources:
* [Stack exchange thread on converging](https://mattermodeling.stackexchange.com/questions/1896/k-points-and-encut-convergence-tests-before-or-after-relaxation) (see answer by Andrew Rosen)
* [VASP-tutor convergence testing](https://dannyvanpoucke.be/vasp-tutor-convergence-testing-en/)
* [Do I need spin polarization?](https://www.researchgate.net/post/Do_I_need_to_consider_spin_polarization_when_calculating_the_pristine_CeO2_surface)

## Numerical Convergence

* `Algo = Damped` works best with HSE calculations. `Algo = Normal` can be very slow.
* If convergence isn't reached with `Algo = Damped`, try reducing `TIME`.
* Usually, if the calculation doesn't converge within `NELM = 50-60` it's not going to.
* Can set `IMIX = 1` and adjust `AMIX` and `BMIX`. VASP recommends only adjusting `BMIX` with `IMIX = 1`.
* Lowering `POTIM` from the default value of 0.5 slows down the atomic relaxation steps and can help with convergence.
