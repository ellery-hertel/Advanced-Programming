# Ellery Hertel

def check_text_length(message): #evaluates whether a string is too long
    if len(message) > 140:
        return "The text message is too long."
    else: #if the string is not too long, it will return the string
        return message

print(check_text_length("Do you think this text message is too long?"))