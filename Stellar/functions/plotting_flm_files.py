#CALLED IN HET_spectra_plots.py

#imports for plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np #needed for tick marks settings

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET using LRS device
#Rest wavelength, scaled flux, error in scaled flux

x = [ ] #rest wavelength
y = [ ] #scaled flux
yerr = [ ] #flux-error

#function made with no call here since call in other file
#n pull file data, m pulls plot name
def fml_plt(n, m):
    #open process from Comp Phys course - 3340_c_f26_deberry.ipynb
    with open(n, 'r') as data:
        for line in data:
            #split process from python documentation and strip from Comp Phys Course - simple split to break data at space/tab
            sline=line.strip().split()
            x.append(sline[0])
            y.append(sline[1])
            yerr.append(sline[2])

    #plot data with days pulled from call file
    plt.plot(x,y)
    plt.title(f'HET_{m}_days_from_discovery.flm')
    plt.xlabel('Rest Wavelength')
    plt.ylabel('Scaled Flux')
    plt.show()
