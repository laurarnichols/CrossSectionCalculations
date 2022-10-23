# Parallelization and Memory

* To determine the number of processors:
  * Figure out how many electrons are in the system by adding up the occupations for each atom type and multiplying by how many atoms of that type are in the system
  * Divide by 10
  * Get node count by dividing the number of processors per node and rounding up
  * Multiply the rounded number of nodes by the number of processors per node
  * For HSE calculations, multiply by 2 or 3
* Hybrid MPI/OpenMP
  * To optimize the number of threads per process, look at the die layout on [wikichip](https://en.wikichip.org/wiki/intel)
  * The Excalibur nodes use Intel Xeon E5 chips which have groups of 4 cores with a total of 32 cores per node
  * It is best to keep a single group together with OpenMP because it is a shared memory paradigm
  * For the PBS queue system, use 

```#PBS -l select=num. nodes:ncpus=cores/node:mpiprocs=MPI procs/node:ompthreads=threads/MPI proc
-n is the number of MPI processes (nodes*MPI proc/node)
-N is the number of MPI processes per node
-d is the number of OpenMP threads per MPI process
```

* If a job is running out of memory, a common trick is to double the number of nodes and half the amount of MPI processes per node. The total number of processes for the job (`-n`) stays the same, but each processes now has access to more memory.
* Can find the number of unique k points by running a calculation quickly (wall clock of 1-5 minutes) and looking at the output file. Then you can determine good parallelization parameters.

## VASP

* `NCORE`
  * Sets the number of bands per group
  * Related to `NPAR`, which is the number of bands that are treated in parallel
  * Recommended setting is `NPAR = sqrt(number-of-cores)` or `NCORE = cores-per-node`
  * The relationship between `NPAR` and `NCORE` is `NCORE = number-of-cores/KPAR/NPAR`
  * Andy has found that, for the system sizes we typically work with (~100-atom supercells), `NCORE=~16` is good for PBE and `NCORE=~4` is good for HSE
  * Ideally, `NCORE` should be a factor of `cores-per-node`, since this reduces communication between nodes
  * `NBANDS` and `NCORE` should line up as follows
    * Take the number of cores and divide by `NCORE` to get the number of band groups
    * The number of bands must be evenly divisible by the number of band groups
    * If these values don't line up, VASP will automatically adjust the numbers of bands, which can lead to issues if you are setting the occupations manually using `FERWE/FERDO`
  * Lower (higher) `NCORE` is slower (faster) but utilizes less (more) memory
* `KPAR`
  * Should be an integer divisor of the total number of cores
  * K-points are split up first, then bands
  * Number of processors working on a group of k-points is `number-of-cores/KPAR`
  * Try not to let the number of processors working on a group split across nodes (i.e., make `number-of-cores/KPAR` an integer divisor of the number of cores per node
  * Also, try to have the same number of k-pooints in each group (i.e., make `KPAR` an integer divisor of the number of unique k-points)
  * To be safe, you can set the bands and processors based on `NCORE`, then set `KPAR` based on number of k-points and multiply the number of nodes by `KPAR`


## QE

* See [this guide from QE](https://www.quantum-espresso.org/Doc/user_guide/node18.html) and [this powerpoint](https://hpc-forge.cineca.it/files/CoursesDev/public/2016/Bologna/Material_Science_codes_on_innovative_HPC_architectures/CorsoMAX-PRACE-QE-Parallelization.pdf)
* For k-point parallelization, default the number of cores to a divisor of the number of k-points if possible
* When setting the number of k-point pools, multiply the number of original processors by the number of pools
* Set the number of band groups using `-nb n` where `n` is calculated by the number of processors divided by the number of bands per group you want
* Make sure that the `nbnd` tag in the input file is divisible by the `-nb` tag in the job script
* `-nb` is particularly useful for speeding up hybrid calculations


