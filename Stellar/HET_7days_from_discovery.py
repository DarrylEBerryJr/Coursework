import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import csv

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET at LRS
#Rest wavelength, scaled flux, error

x = []
y = []
yerr = []

def main():

    with open('/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_7days_from_discovery.flm', 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=' ')

        for rows in plotting:
            x.append(rows[0])
            y.append(rows[1])
            yerr.append(rows[3])

    xy()

def xy():
    plt.plot(x,y)
    plt.title('HET_7days_from_discovery.flm')
    plt.xlabel('Column 1')
    plt.ylabel('Column 2')
    plt.show()

main()
