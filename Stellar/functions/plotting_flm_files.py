#imports for plotting
import matplotlib as mpl
import matplotlib.pyplot as plt

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET using LRS device
#Rest wavelength, scaled flux, error in scaled flux

x = [ ] #rest wavelength
y = [ ] #scaled flux
yerr = [ ] #flux-error

#function made with no call for call in other file
def HET_7(n):
    #open process from Comp Phys course - 3340_c_f26_deberry.ipynb
    with open(n, 'r') as data:
        for line in data:
            #split process from python documentation and strip from Comp Phys Course
            sline=line.strip().split()
            x.append(sline[0])
            y.append(sline[1])
            yerr.append(sline[2])

    plt.plot(x,y)
    plt.title('HET_7days_from_discovery.flm')
    plt.xlabel('Rest Wavelength')
    plt.ylabel('Scaled Flux')
    plt.show()

#function made with no call for call in other file
def HET_10(n):
    #open process from Comp Phys course - 3340_c_f26_deberry.ipynb
    with open(n, 'r') as data:
        for line in data:
            sline=line.strip().split()
            x.append(sline[0])
            y.append(sline[1])
            yerr.append(sline[2])

    plt.plot(x,y)
    plt.title('HET_10days_from_discovery.flm')
    plt.xlabel('Rest Wavelength')
    plt.ylabel('Scaled Flux')
    plt.show()

#Code by Darryl E Berry Jr (c) 2026
#2nd Year PhD Student - SMU