# Ellery Hertel

import math

def check_temp(x) :
    if x > 78:
        print("Turn on the AC!")
    elif x < 62:
        print("Turn on the heat!")
    elif 62 <= x <= 78:
        print("It's wonderful weather!")