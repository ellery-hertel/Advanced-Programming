# Ellery Hertel

fruits = ["cherry", "pomegranate", "apple", "cherry", "banana", "apple", "orange", "banana", "cherry"]

for x in fruits: #reads each item in fruits
    if x == "cherry":
        print("I cherry-ish you!")
    elif x == "banana":
        print("Banana, it is!")
    elif x == "apple":
        print("You are the apple of my eye!")
    else: #considers the possibility that it's none of fruits we wanted to read
        print("Objection!")