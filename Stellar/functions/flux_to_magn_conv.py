#external function to convert flux to magnitude
#ref RKehoe TimeDomainProjLightcurves.pdf
#ref https://numpy.org/doc/stable/reference/generated/numpy.log10.html

import numpy as np

#Flux = [energy/area/time] = [erg / cm^2 / s]

x_7 = [ ]
x_10 = [ ]

y_7 = [ ] #scaled flux HET7
y_10 = [ ] #scaled flux HET10

yerr_7 = [ ] #y-error 7
yerr_10 = [ ] #y-error 10


'''def magn_to_flux_conv():
    F = F_0 * 10**(-0.4 * (delta_m)) #delta_m = m - m_0
    return F'''

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET at LRS
#Rest wavelength, scaled flux, error

#function made with no call for call in other file
def get_magn():

    file7 = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_7days_from_discovery.flm'

    with open(file7, 'r') as data:
        for line in data:
            #split process from python documentation and strip from Comp Phys Course
            sline_7=line.strip().split()
            x_7.append(sline_7[0])
            y_7.append(sline_7[1])
            yerr_7.append(sline_7[2])

    np_x_7 = np.array(x_7)
    np_y_7 = np.array(y_7)
    np_yerr_7 = np.array(yerr_7)

    file10 = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_10days_from_discovery.flm'

    with open(file10, 'r') as data:
        for line in data:
            sline_10=line.strip().split()
            x_10.append(sline_10[0])
            y_10.append(sline_10[1])
            yerr_10.append(sline_10[2])
            
    np_x_10 = np.array(x_10)
    np_y_10 = np.array(y_10)
    np_yerr_10 = np.array(yerr_10)

    F_0_7 = np_y_7
    F_7 = np_x_7
    
    delta_m = -2.5 * np.log10(np.divide(F_7, F_0_7)) #delta_m = m - m_0
    print(delta_m)


get_magn()