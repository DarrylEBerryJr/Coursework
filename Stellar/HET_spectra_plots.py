#for later math
import numpy as np

#function made in separate file to call for plotting all flm files
#plotting_flm_files.py
from functions.plotting_flm_files import HET_7, HET_10
#method from https://www.geeksforgeeks.org/python/python-call-function-from-another-file/
#https://stackoverflow.com/questions/65419934/access-function-in-other-python-file-within-a-subfolder

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET using LRS
#Rest wavelength, scaled flux, error

which = input("Which data to plot? ")

if which == "7":
    HET_7()
if which == "10":
    HET_10()




#Code by Darryl E Berry Jr (c) 2026
#2nd Year PhD Student - SMU