# Ellery Hertel

def count_o(word): #counts the number of "o"s in a word or string
    char = "o"
    count = 0
    for x in word:
        if x == char: #finds all the "o"s in the string
            count += 1
    return count


print(count_o("bonobos"))