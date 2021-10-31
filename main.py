# Import modules needed
import string, random

def generatePass(length: int, useSpecialCharacters: bool):
    characters = string.ascii_letters + string.digits
    if useSpecialCharacters:
        characters += "!@#$%^&*()"

    password = []
    for _ in range(length):
        # Randomly select character and add it to password
        password.append(random.choice(list(characters)))

    # Shuffle the password
    random.shuffle(password)

    return "".join(password)

# Console prompt
length = int(input("Enter password length: "))
# You decide whether to use special characters or not
choice = input("Use special characters? (y/n): ")

specialChars = False
if choice.lower() == "y":
    specialChars = True

# Generate the password
password = generatePass(length, specialChars)
# Print the password
print("Your password:", password)