#Called in magnitude_comparison.py 
 
# #Computational Physics 2nd Ed by Mark Newman, Section 5.1.1
#v band 5510 Angstroms plus/minus 880 Angstroms - http://astro.vaporia.com/start/v.html
#SciPy modules - trapezoid - https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapezoid.html

import numpy as np
from scipy import integrate
# trapezoid(y, x=None, dx=1.0, axis=-1)

'''
Parameters
:
y
array_like
Input array to integrate.
x
array_like, optional
The sample points corresponding to the y values. If x is None, the sample points are assumed to be evenly spaced dx apart. The default is None.
dx
scalar, optional
The spacing between sample points when x is None. The default is 1.
axis
int, optional
The axis along which to integrate. The default is the last axis.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapezoid.html#r08b19396d7a1-2
'''



x = [ ] #points corresponding to the y values (first column)
y = [ ] #array input to integrate (second column)
z = [ ] #error of second column (third column)

npx = [ ]
npy = [ ]
npz = [ ]

#function made with no call here since call in other file
#n pull file data, m pulls plot name
def get_value(n):
    #open process from Comp Phys course - 3340_c_f26_deberry.ipynb
    with open(n, 'r') as data:
        for line in data:
            #split process from python documentation and strip from Comp Phys Course - simple split to break data at space/tab
            sline=line.strip().split()
            x.append(sline[0])
            y.append(sline[1])
            z.append(sline[2])

        #Convert array of strings to numbers - https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
        for i in range(len(x)):
            t = float(x[i])
            npx.append(t)

        for j in range(len(y)):
            u = float(y[j])
            npy.append(u)

        for k in range(len(z)):
            v = float(z[k])
            npz.append(v)

    trap_int(npx, npy, npz)

def trap_int(a, b, c):
    print(integrate.trapezoid(b, a))


