# `SiVH3_paperQE`

This set of calculations is meant to reproduce the matrix elements from the original Barmparis paper. The system is a triply-hydrogenated silicon vacancy, and PBE functionals are used.

## Notes

* Relaxing neutral defect fit in the debug queue (`walltime=1:00:00`) with 2 nodes, 44 processors each, but relaxing neutral pristine needed 3 nodes to fit in the debug queue
* Can't use `-nk` option on Export currently. Need to see if I can make this work because output in `Export` is currently serial. 
* Both exports took about 4.5 hours with 2 nodes, 44 processors each (not sure if parallel helps the rest of the code that's not output)
* `TME` took 2.5 hours on 4 nodes with 44 processors each
