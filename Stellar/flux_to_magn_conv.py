#external function to convert flux to magnitude
#ref RKehoe TimeDomainProjLightcurves.pdf
#ref https://numpy.org/doc/stable/reference/generated/numpy.log10.html

import numpy as np

#Flux = [energy/area/time] = [erg / cm^2 / s]

def flux_to_magn_conv():
    m - m_0 = -2.5 * np.log10(F / F_0)

def magn_to_flux_conv():
    F = F_0 * 10**(-0.4 * (m - m_0))