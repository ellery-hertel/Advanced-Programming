# Ellery Hertel

import math

def maxnumber(x, y, z) :
    if x == y == z:
        print("All are equal.")
    elif y < x and z < x:
        print(x, "is greatest.")
    elif x < y and z < y:
        print(y, "is greatest.")
    elif x < z and y < z:
        print(z, "is greatest.")

maxnumber(2, 25, 17)