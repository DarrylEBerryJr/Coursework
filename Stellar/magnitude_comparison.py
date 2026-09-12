#function made in separate file to call for getting magnitude via trapesoid
#trapezoid_integration.py

from functions.trapezoid_integration import *

#method from https://www.geeksforgeeks.org/python/python-call-function-from-another-file/
#https://stackoverflow.com/questions/65419934/access-function-in-other-python-file-within-a-subfolder
#sending plot title from user input with f-string: https://stackoverflow.com/questions/73143269/how-to-set-a-figure-title-from-a-user-input
#changing tick frequency - https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-the-x-or-y-axis


#sn1ph flm files are photometry data - light curve from ROTSE-IIIb telescope
#Modified Julian Date (MJD), magnitude, error

#list of files to print
bol_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1ph/bol_lc_full_cor.dat'
sn_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1ph/sn-lc_rotse_psf.dat'
HET_7_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_7days_from_discovery.flm'
HET_10_file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_10days_from_discovery.flm'


#choose which file to print
which = input("Enter 'bol' for a bolometric file and 'sn' for the supernova file, 7 for HET_7 file, and 10 for HET_10 file: ").lower().strip()

#sends to function file the file data and plot title
if which == "bol":
    get_value(bol_file)
if which == "sn":
    get_value(sn_file)
if which == "7":
    get_value(HET_7_file)
if which == "10":
    get_value(HET_10_file)

#Code by Darryl E Berry Jr (c) 2026
#2nd Year PhD Student - SMU