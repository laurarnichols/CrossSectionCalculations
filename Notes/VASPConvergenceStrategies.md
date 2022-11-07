# VASP Convergence Strategies

* `Algo = Damped` works best with HSE calculations. `Algo = Normal` can be very slow.
* If convergence isn't reached with `Algo = Damped`, try reducing `TIME`.
* Usually, if the calculation doesn't converge within `NELM = 50-60` it's not going to.
* Can set `IMIX = 1` and adjust `AMIX` and `BMIX`. VASP recommends only adjusting `BMIX` with `IMIX = 1`.
* Lowering `POTIM` from the default value of 0.5 slows down the atomic relaxation steps and can help with convergence.
