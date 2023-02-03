# Si-H Potential

This calculation is to look at the total energy curve as a function of Si-H bond length to get an idea of how quickly (in length and vibrational quanta) the bond gets anharmonic. 

Choosing the bond betwen Si 107 and H 216. From VESTA, we have
```
Bond: l(Si107-H1) =  1.49062(0) Å
 107   Si107 Si  0.51044  0.33168  0.50758 ( 0, 0, 0)+ x, y, z
 216      H1  H  0.46466  0.38710  0.45206 ( 0, 0, 0)+ x, y, z
```

The lattice vectors are
```
    16.4117625311398250    0.0000347833292740    0.0000000000000000
     0.0000347833292740   16.4117625311398250    0.0000000000000000
     0.0000000000000000    0.0000000000000000   16.4117624058248701
```
so the cartesian coordinates are 
```
Si -- 8.37722 5.44345 8.33028
H -- 7.62589 6.35299 7.41910
```

The unit vector pointing from Si to H is then `(-0.75133, 0.90954, -0.91118)`, or in unit length `(-0.50403, 0.61017, -0.61127)`. Going to consider 3 positions of the H closer to Si and 5 positions further out. All positions of the H atom in direct coordinates are
```
0.47387 0.37595 0.46323
0.47080 0.37966 0.45951
0.46773 0.38338 0.45579
0.46466 0.38710 0.45206 (equilibrium)
0.46159 0.39082 0.44834
0.45852 0.39454 0.44461
0.45545 0.39825 0.44089
0.45238 0.40197 0.43716
0.44930 0.40569 0.43344
```

The resulting total energies are 
```
-1170.31429616
-1171.07865896
-1171.43959399
-1171.53663541 (equilibrium)
-1171.46615680
-1171.29440609
-1171.06824634
-1170.82017855
-1170.57530569

```
