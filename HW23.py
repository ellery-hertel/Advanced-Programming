# Ellery Hertel

import math

def min_number(x, y, z) :
    if x == y == z:
        print("All are equal.")
    elif x < y and x < z:
        print(x, "is smallest.")
    elif y < x and y < z:
        print(y, "is smallest.")
    elif z < x and z < y:
        print(z, "is smallest.")

min_number(206, 405, 112)