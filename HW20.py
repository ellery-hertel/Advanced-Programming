# Ellery Hertel

import math

def calculate_grade(x) :
    if 93 <= x <= 100:
        grade = "A"
        return grade
    elif 90 <= x <= 92:
        grade = "A-"
        return grade
    elif 87 <= x <= 89:
        grade = "B+"
        return grade
    elif 83 <= x <= 86:
        grade = "B"
        return grade
    elif 80 <= x <= 82:
        grade = "B-"
        return grade
    elif 77 <= x <= 79:
        grade = "C+"
        return grade
    elif 73 <= x <= 76:
        grade = "C"
        return grade
    elif 70 <= x <= 72:
        grade = "C-"
        return grade
    elif 65 <= x <= 69:
        grade = "D+"
        return grade
    elif 55 <= x <= 64:
        grade = "D"
        return grade
    elif 50 <= x <= 54:
        grade = "D-"
        return grade
    elif x <= 49:
        grade = "F"
        return grade
