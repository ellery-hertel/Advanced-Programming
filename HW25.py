# Ellery Hertel

import math

def check_odd(x) :
    if x % 2 == 0:
        return False
    else:
        return True

def sum_of_odd(a, b) :
    if a + 1 == b or a == b:
        return 0
    elif a > b:
        print("Please choose b greater than a.")
    elif (a + 1) < b:
        if check_odd(a):
            a = a + 2
            sum = a + sum_of_odd(a, b)
            return sum
        else:
            a = a + 1
            sum = a + sum_of_odd(a, b)
            return sum

print(sum_of_odd(2, 14))