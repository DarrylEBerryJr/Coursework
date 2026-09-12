#function made in separate file to call for plotting all flm files
#plotting_dat_files.py
from functions.plotting_dat_files import phot_plt
#method from https://www.geeksforgeeks.org/python/python-call-function-from-another-file/
#https://stackoverflow.com/questions/65419934/access-function-in-other-python-file-within-a-subfolder
#sending plot title from user input with f-string: https://stackoverflow.com/questions/73143269/how-to-set-a-figure-title-from-a-user-input
#changing tick frequency - https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-the-x-or-y-axis


#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET using LRS
#Rest wavelength, scaled flux, error

#list of files to print
bol_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1ph/bol_lc_full_cor.dat'
sn_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1ph/sn-lc_rotse_psf.dat'

#choose which file to print
which = input("Enter 'bol' for a bolometric file and 'sn' for the supernova file: ").lower().strip()

#sends to function file the file data and plot title
if which == "bol":
    phot_plt(bol_file, 'bol_lc_full_cor')
if which == "sn":
    phot_plt(sn_file, 'sn-lc_rotse_psf')

#Code by Darryl E Berry Jr (c) 2026
#2nd Year PhD Student - SMU