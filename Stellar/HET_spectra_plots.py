#for later math
import numpy as np

#function made in separate file to call for plotting all flm files
from plotting_flm_files import HET_7, HET_10

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET at LRS
#Rest wavelength, scaled flux, error

which = input("Which data to plot? ")

if which == "7":
    HET_7()
if which == "10":
    HET_10()