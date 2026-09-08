import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import csv

x = []
y = []
z = []

def main():

    with open('/Users/debj/Documents/code/Coursework/Stellar/x371/deberry/sn1sp/HET_10days_from_discovery.flm', 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=' ')

        for rows in plotting:
            x.append(rows[0])
            y.append(rows[1])
            z.append(rows[2])

    chart = input("xy, xz, or yz: ")

    if chart == "xy":
        print("Graph x=Column 1, y=Column 2")
        xy()
    elif chart == "xz":
        print("Graph x=Column 1, y=Column 3")
        xz()
    else:
        print("Graph x=Column 2, y=Column 3")
        yz()

def xy():
    plt.plot(x,y)
    plt.title('HET_10days_from_discovery.flm')
    plt.xlabel('Column 1')
    plt.ylabel('Column 2')
    plt.show()

def xz():
    plt.plot(x,z)
    plt.title('HET_10days_from_discovery.flm')
    plt.xlabel('Column 1')
    plt.ylabel('Column 3')
    plt.show()

def yz():
    plt.plot(y,z)
    plt.title('HET_10days_from_discovery.flm')
    plt.xlabel('Column 2')
    plt.ylabel('Column 3')
    plt.show()

main()
