#function made in separate file to call for plotting all flm files
#plotting_flm_files.py
from functions.plotting_flm_files import fml_plt
#method from https://www.geeksforgeeks.org/python/python-call-function-from-another-file/
#https://stackoverflow.com/questions/65419934/access-function-in-other-python-file-within-a-subfolder

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET using LRS
#Rest wavelength, scaled flux, error

#list of files to print
HET_7_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_7days_from_discovery.flm'
HET_10_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_10days_from_discovery.flm'

#choose which file to print
which = input("Which data to plot? Input '7' for HET7 and '10' for HET10: ")

#sends to function file the file data and plot title
if which == "7":
    fml_plt(HET_7_file, 7)
if which == "10":
    fml_plt(HET_10_file, 10)

#Code by Darryl E Berry Jr (c) 2026
#2nd Year PhD Student - SMU7
