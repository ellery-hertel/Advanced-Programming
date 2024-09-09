# Ellery Hertel

import math

def distance(lat1, long1, lat2, long2) :
    dlat = lat2 - lat1
    dlong = long2 - long1
    dsquared = dlat**2 + dlong**2
    result = math.sqrt(dsquared)
    return result