# How to Compile QE
* Load `gnu` environment (`PrgEnv-gnu`)
* `module load fftw`
* `module load cray-libsci`
* Make sure QE is extracted from `.tar.gz` file and change into directory
* Run `./configure`
* Make the following changes to the `make.sys` file
  * Remove `-D__SCALAPACK` from `DFLAGS`, if there
  * Uncomment `F90` declaration
  * Match compilers (`MPIF90`, `F90`, `cc`, `F77`, `CPP`) with the machine specifications (e.g., the compilers listed in the User Guide for a specific [DOD HPC machine](https://centers.hpc.mil/systems/unclassified.html))
  * `FFLAGS = -fcheck=all -O3 -g -dynamic`
  * `LDFLAGS = -g -pthread -dynamic`
  * Update the libaries for the specific machine
    * Onyx:
      * `BLAS_LIBS = -L/opt/intel/compilers_and_libraries_2020.4.304/linux/mkl/lib/intel64`(`external`)
      * `LAPACK_LIBS = $(TOPDIR)/lapack-3.2/lapack.a` (`internal`)
      * `FFT_LIBS = -L/opt/cray/pe/fftw/3.3.8.5/haswell/lib`
* Run `make pw pp` to compile
