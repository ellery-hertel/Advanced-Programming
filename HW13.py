# Ellery Hertel

# finds the area outside a circle contained within a square by calculating area of square
# and of circle, then subtracting circle area from square area

import math

x = math.pi
def area_circle(radius) :
    print(x * radius ** 2)


def area_square(length, width) :
    print(length * width)


def area_between(area_square, area_circle) :
    print("The area outside the circle and within the square is", area_square - area_circle, ".")