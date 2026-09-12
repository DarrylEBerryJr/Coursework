#function made in separate file to call for plotting all flm files
#plotting_dat_files.py
from functions.plotting_dat_files import bol, sn
#method from https://www.geeksforgeeks.org/python/python-call-function-from-another-file/
#https://stackoverflow.com/questions/65419934/access-function-in-other-python-file-within-a-subfolder

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET using LRS
#Rest wavelength, scaled flux, error

which = input("Which data to plot? Enter 'bol' for a bolometric file and 'sn' for the supernova file: ").lower().strip()

bol_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1ph/bol_lc_full_cor.dat'

sn_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1ph/sn-lc_rotse_psf.dat'


if which == "bol":
    bol(bol_file)
if which == "sn":
    sn(sn_file)

#Code by Darryl E Berry Jr (c) 2026
#2nd Year PhD Student - SMU