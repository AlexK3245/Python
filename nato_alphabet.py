# This assignment is to have a dictionary of the NATO alphabet,
# and then get a user input of a word and spell it using the Nato alphabet


def spell_word():
    # This function will get a word from the user and then convert it to the Nato alphabet
    word = input("Enter a word: ")
    user_word = word.upper()
    # print(f"{user_word}")
    for letter in user_word:
        print(nato_alphabet[letter])


def main():
    # This function calls the spell_word() function which then makes the program work
    spell_word()


nato_alphabet = {"A": "Alpha",
                 "B": "Bravo",
                 "C": "Charlie",
                 "D": "Delta",
                 "E": "Echo",
                 "F": "Foxtrot",
                 "G": "Golf",
                 "H": "Hotel",
                 "I": "India",
                 "J": "Juliette",
                 "K": "Kilo",
                 "L": "Lima",
                 "M": "Mike",
                 "N": "November",
                 "O": "Oscar",
                 "P": "Papa",
                 "Q": "Quebec",
                 "R": "Romeo",
                 "S": "Sierra",
                 "T": "Tango",
                 "U": "Uniform",
                 "V": "Victor",
                 "W": "Whiskey",
                 "X": "X-Ray",
                 "Y": "Yankee",
                 "Z": "Zulu"}


main()
