# Ellery Hertel

# calculates a mathematical formula for maturity given input time, temp, and ratio

import math

def maturity(time, temp, ratio) :
    print((23.7 * (time ** 3)) + (temp / 273) + math.log(ratio))
