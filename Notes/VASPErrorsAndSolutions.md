# VASP Errors and Solutions

These are some errors I have encountered in VASP and how I addressed them.

* _Error reading item 'VCAIMAGES' from file INCAR._ usually means that the INCAR file doesn't exist where VASP is trying to read it. This can happen if you don't have an INCAR in your directory or if the path to your folder is incorrect in the PBS script.
