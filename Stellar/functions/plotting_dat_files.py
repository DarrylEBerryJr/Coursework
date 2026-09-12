#imports for plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np  #needed for tick marks setting

#sn1ph dat files are photometry data from ROTSE-IIIb
#MJD (date), magnitude, error in magnitude

x = [ ] #rMJD
y = [ ] #magnitude
yerr = [ ] #magn-error

#functions made with no call for call in other file
#recieves whatever data file from function call no need to edit per file change

def bol(n):

    #open process from Comp Phys course - 3340_c_f26_deberry.ipynb
    with open(n, 'r') as data:
        for line in data:
            #split process from python documentation and strip from Comp Phys Course
            sline=line.strip().split()
            x.append(sline[0])
            y.append(sline[1])
            yerr.append(sline[2])

    plt.plot(x,y)
    plt.title('Bolometric Data From dat File')
    plt.xlabel('MJD')
    plt.ylabel('Magnitude')
    plt.xticks(np.arange(1, 300, 10))
    plt.yticks(np.arange(1, 300, 10))
    plt.show()
    #click the magnifying glass on the plot menu to drag an area and zoom in on that selected part of the plot

def sn(n):

    #open process from Comp Phys course - 3340_c_f26_deberry.ipynb
    with open(n, 'r') as data:
        for line in data:
            #split process from python documentation and strip from Comp Phys Course
            sline=line.strip().split()
            x.append(sline[0])
            y.append(sline[1])
            yerr.append(sline[2])

    plt.plot(x,y)
    plt.title('SN Data From dat File')
    plt.xlabel('MJD')
    plt.ylabel('Magnitude')
    plt.xticks(np.arange(1, 300, 15))
    plt.yticks(np.arange(1, 300, 15))

    plt.show()
    #click the magnifying glass on the plot menu to drag an area and zoom in on that selected part of the plot

#Code by Darryl E Berry Jr (c) 2026
#2nd Year PhD Student - SMU