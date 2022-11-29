# LAMMPS

LAMMPS is an MD software. We use LAMMPS to relax the amorphous $\text{SiO}\_2$ in our prototype dangling bond system. 

## Resources
* [Various tutorials](https://lammpstutorials.github.io/)
* [Manual](https://docs.lammps.org/)
* [Example input file](https://docs.lammps.org/2001/data_format.html)
* [Potentials](lammps.sandia.gov/bench.html#potentials)

## Commands

### Initialization

* [`units`](https://docs.lammps.org/units.html)
  * Sets the units for the calculation
  * Best to use `metal` for our purposes for Ang and eV
* [`atom_style`](https://docs.lammps.org/atom_style.html)
  * Determines what information is stored for each atom
  * Best to use `atomic` for solids
* [`dimension`](https://docs.lammps.org/dimension.html)
  * How many dimensions to use in the simulation
  * Default is 3
* [`pair_style`](https://docs.lammps.org/pair_style.html)
  * Sok suggested that we use the Tersoff-style potentials
  * The [Tersoff potential](https://en.wikipedia.org/wiki/Bond_order_potential) is a pairwise potential where the bond strength is modified by the neighborhood of the atoms
* [`boundary`](https://docs.lammps.org/boundary.html)
  * Determines boundary conditions in each direction
  * Default is `boundary p p p` for all periodic boundaries
  * We should stick with the default because we plan to integrate with VASP, which uses periodic boundary conditions

### System Definition

* [`lattice`](https://docs.lammps.org/lattice.html)
  * Defines the lattice parameter and vectors
  * For specific cell types, you can give the cell type and lattice parameter:
    * `lattice fcc 3.52`
    * `lattice diamond 5.431`
  * For a custom cell type, you can set the lattice vectors explicitly:
    * Use `a1`, `a2`, and `a3` to set the lattice vectors
    * Use `basis` to set the fractional coordinates of a basis atom
    * `lattice custom 3.52 a1 1.0 0.0 0.0 a2 0.5 1.0 0.0 a3 0.0 0.0 0.5 basis 0.0 0.0 0.0 basis 0.5 0.5 0.5`
* [`region`](https://docs.lammps.org/region.html)
  * Defines different regions in the simulation
  * We will use this to define our cell
  * First argument is the name of the region
  * Second argument gives shape/style of region 
  * We will use `block x_min x_max y_min y_max z_min z_max`
* [`create_box`](https://docs.lammps.org/create_box.html)
  * Generates the simulation box
  * First argument is the number of atom types
  * Second argument is the `region` name to use to create the box
* [`create_atoms`](https://docs.lammps.org/create_atoms.html)
  * Alternative to reading atom coordinates using `read_data` or `read_restart`
  * Simulation box must already exist (typically created with `create_box`)
  * Lattice must also be defined via `lattice`
  * First argument is index of atom type to create
  * Second arugment is style
  * For `box` style, lattice is populated within simulation box
* [`read_data`](https://docs.lammps.org/read_data.html)
  * Read initial atom coordinates and other parameters from input file
  * `read file-name`
* [`pair_coeff`](https://docs.lammps.org/pair_coeff.html)
  * First two arguments are atom types for the given coefficient
  * Can use asterisks for first two arguements
  * Can overwrite more-general coefficients defined with asterisks later in script
  * For tersoff `pair_style`:
    * First two arguments must be asterisks
    * Third argument is file name (found in `LAMMPS_POTENTIALS` path)
    * Final arguments are how you would like the atoms found in the potential file to map onto the atom types previously defined
    * Example: if you have 3 atom types and you want the first two to be Si and the last one to be C, you would use `pair_coeff * * SiC.tersoff Si Si C`
* [`mass`](https://docs.lammps.org/mass.html)
  * Set masses of atoms
  * First argument is atom-type index or label
  * Second argument is the mass
  * Can use an aterisk when using indices to define several atom types with the same mass
  * For label:
    * `labelmap atom 1 C`
    * `mass C 12.01`
    * Can also use label if defined in input file
  * Defined in same way in input file
    * Follows `Masses` header
    * `atom-type mass`
    * Can't use asterisk in input file

### Simulation Settings

* [`velocity`](https://docs.lammps.org/velocity.html)
  * First argument is group ID (e.g., `all`)
  * Second arguemnt determines the style of how to set the velocities
  * A style of `create` generates a random set of velocities using a temperature and seed (e.g., `create 1000.0 376847`)
  * `loop geom` sets specific seeds for each atom based on the coordinates. Will not necessarily be the same on all machines because of small numerical differences in coordinates.
* [`neighbor`](https://docs.lammps.org/neighbor.html)
  * Sets the additional distance beyond the force cutoff distance to consider nearest neighbors
  * `neighbor skin style`
  * `style = bin` will almost always be fastest for our purposes
  * For `metal` units, default is `skin = 2.0` Angstroms
* [`neighbor_modify`](https://docs.lammps.org/neigh_modify.html)
  * `delay n` says only consider rebuilding the neighbor list `n` steps after the last build
  * `every n` says consider rebuilding the neighbor list every `n` steps after the `delay` has passed
  * `check yes/no` determines whether or not to check how far atoms have moved before rebuilding neighbor list
  * Default is `check yes`
  * If `check yes`, build only occurs if at least one atom has moved more than half the neighbor skin distance
* [`fix 1 all nve`](https://docs.lammps.org/fix_nve.html) performs plain time integration to update position and velocity using velocity-Verlet algorithm (not invoked during energy minimization)
* [`timestep x`](https://docs.lammps.org/timestep.html) sets the simulation timestep to `x`
* [`run n`](https://docs.lammps.org/run.html) runs the simulation for `n` steps


## Example: Bulk Si

The input script for bulk Si using the Tersoff potential is given in the [LAMMPS potentials list](https://www.lammps.org/bench.html#potentials):
```
# bulk Si via Tersoff

units   metal
atom_style  atomic

lattice   diamond 5.431
region    box block 0 20 0 20 0 10
create_box  1 box
create_atoms  1 box

pair_style  tersoff
pair_coeff  * * Si.tersoff Si
mass            1 28.06

velocity  all create 1000.0 376847 loop geom

neighbor  1.0 bin
neigh_modify    delay 5 every 1

fix   1 all nve

timestep  0.001

run   100
```
