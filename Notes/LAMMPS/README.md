# LAMMPS

LAMMPS is an MD software. We use LAMMPS to relax the amorphous $\text{SiO}\_2$ in our prototype dangling bond system. 

## Resources
* [Various tutorials](https://lammpstutorials.github.io/)
* [Manual](https://docs.lammps.org/)
* [Example input file](https://docs.lammps.org/2001/data_format.html)

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
