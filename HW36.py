# Ellery Hertel

def check_first_letter(x): #checks whether the first letter of a string is k (upper or lower case)
    if x[0] == "k" or x[0] == "K":
        return True
    else:
        return False

print(check_first_letter("Knives are sharp!"))