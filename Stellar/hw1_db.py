import numpy as np

H = 10000 * 1.008
He = 1000 * 4.026
O = 8 * 15.999
C = 4 * 12.011
N = 1 * 14.007
Ne = 1 * 20.180

elements = [H, He, O, C, N, Ne]

print("")
print("Relative number of atoms in Sun times Atomic Mass from periodic table: ")
print(elements)
print("")

e = np.e
u = 1.66 * 10**-27
M = 1.99 * 10**30

print("Constants:")
print("e = ", e)
print("u = ", u, "kg (converts atomic mass to kg)")
print("Solar Mass = ", M, "kg")
print("")

print("Element relative masses in Sun = relative number of atoms * atomic mass * u:")
for value in elements:
    kg = value * u 
    print(kg)
#I know there is a way to add this into another array or list
print("")

total_unit_mass = (H * u) + (He * u) + (O * u) + (C * u) + (N * u) + (Ne * u)
print("Element relative masses in Sun all added together:")
print("total_unit_mass = ", total_unit_mass, "kg")
print("")

num_helpings = M / total_unit_mass
print("Mass of Sun divided by Total unit mass gives number of helpings in Sun:")
print("num_helpings = ", num_helpings)
print("")

print("Mass of each element is element relative mass times number of helpings:")
Total_mass_of_H =  (H * u) * num_helpings
Total_mass_of_He = (He * u) * num_helpings
Total_mass_of_O = (O * u) * num_helpings
Total_mass_of_C = (C * u) * num_helpings
Total_mass_of_N = (N * u) * num_helpings
Total_mass_of_Ne = (Ne * u) * num_helpings

print("Total mass of H = ", Total_mass_of_H, "kg")
print("Total mass of He = ", Total_mass_of_He, "kg")
print("Total mass of O = ", Total_mass_of_O, "kg")
print("Total mass of C = ", Total_mass_of_C, "kg")
print("Total mass of N = ", Total_mass_of_N, "kg")
print("Total mass of Ne = ", Total_mass_of_Ne, "kg")
print("")

Totals = [Total_mass_of_H, Total_mass_of_He, Total_mass_of_O, Total_mass_of_C, Total_mass_of_N, Total_mass_of_Ne]
print("Mass Fraction = total mass of species / total mass of gas")

for mass in Totals:
    MF = mass / M
    print(f"{MF:.3f}")