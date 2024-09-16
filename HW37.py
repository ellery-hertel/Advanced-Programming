# Ellery Hertel

def word_triangle(x): #prints a word triangle (could also be used with symbols)
    word_length = len(x)

    while word_length > 0:
        print(x[:word_length]) #prints however many characters word_length is
        word_length -= 1 #reduces the length of the word by 1 character
    return word_length

word_triangle("abracadabra")