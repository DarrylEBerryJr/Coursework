#external function to convert flux to magnitude
#ref RKehoe TimeDomainProjLightcurves.pdf
#ref https://numpy.org/doc/stable/reference/generated/numpy.log10.html

import numpy as np

#Flux = [energy/area/time] = [erg / cm^2 / s]
#integrate over band - https://mfouesneau.github.io/pyphot/pyphot.html
#V band - http://astro.vaporia.com/start/v.html 
#related package - https://mfouesneau.github.io/pyphot/pyphot.html
#flux processing - https://doc.flux.audio/spat-revolution/Spat_Environment_Processing_Effect.html
#using Trapezoid method of integration (from related package page)



F_0_V = 3.55    #E-9 erg/s/cm^2 Johnson Filter System for Vega
F_0_B = 6.20    #E-9 erg/s/cm^2 Johnson Filter System for Vega

m_0_V = 0.044   #Vega
m_0_B = 0.163   #Vega

x_7 = [ ]
x_10 = [ ]

y_7 = [ ] #scaled flux HET7
y_10 = [ ] #scaled flux HET10

yerr_7 = [ ] #y-error 7
yerr_10 = [ ] #y-error 10


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

    file10 = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_10days_from_discovery.flm'

    with open(file10, 'r') as data:
        for line in data:
            sline_10=line.strip().split()
            x_10.append(sline_10[0])
            y_10.append(sline_10[1])
            yerr_10.append(sline_10[2])
            
    m_v = m_0_V - 2.5 * np.log10(np.divide(y_7, F_0_V)) #delta_m = m - m_0
    m_b = m_0_B - 2.5 * np.log10(np.divide(y_7, F_0_V)) #delta_m = m - m_0


    print(m_v)
    print(m_b)

get_magn()