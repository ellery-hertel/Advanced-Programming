# Ellery Hertel

import math

def summation(x,y) :
    if x + 1 == y or x == y:
        return 0
    elif x > y:
        print("Please choose y greater than x.")
    elif (x + 1) < y:
        x = x + 1
        sum = x + summation(x, y)
        return sum


print(summation(1, 5))