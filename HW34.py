# Ellery Hertel NOT WORKING


def read_tweet(tweet): #counts the number of "#" in a tweet
    char = "#"
    count = 0
    for x in tweet:
        if x == char: #counts all the iterations of "#"
            count += 1
    return count

print(read_tweet("#programmingiscool #python"))