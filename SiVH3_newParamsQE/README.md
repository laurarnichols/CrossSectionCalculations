# `SiVH3_newParamsQE`

The system is a triply-hydrogenated silicon vacancy, and PBE functionals are used. This set of calculations was an aim to reproduce the matrix elements from the original Barmparis paper with parameters typically used in VASP. The goal was to have some clarity on the source of changes in the VASP calculations, as the `Export` code is currently untested for VASP. However, the parameters typically used in VASP did not reproduce the original paper results. 

![MatrixElementCompare](https://user-images.githubusercontent.com/32521892/130630677-0855e2c6-8af0-4c34-a8af-a025c1ecb216.png)

## Notes

* QE calculations fit in the debug queue (`walltime=1:00:00`) with 2 nodes, 44 processors each
* Can't use `-nk` option on Export currently. Need to see if I can make this work because output in `Export` is currently serial. 
* Both exports took about 4.5 hours with 2 nodes, 44 processors each (not sure if parallel helps the rest of the code that's not output)
* `TME` took 2.5 hours on 4 nodes with 44 processors each
