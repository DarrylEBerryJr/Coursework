#imports for plotting
import matplotlib as mpl
import matplotlib.pyplot as plt

#sn1sp flm files are spectra data - before, during, and/or after peak (mostly) from HET at LRS
#Rest wavelength, scaled flux, error

x = [ ] #rest wavelength
y = [ ] #scaled flux
yerr = [ ] #y-error

#function made with no call for call in other file
def HET_7():

    file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_7days_from_discovery.flm'

    #open process form Comp Phys course - 3340_c_f26_deberry.ipynb
    with open(file, 'r') as data:
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
def HET_10():

    file = '/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_10days_from_discovery.flm'

    with open(file, 'r') as data:
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
