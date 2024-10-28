"""
        This program will ask the user for a character, and then will output the corresponding ASCII value
    """


def main():
    # This function is the main function of the program
    # The loop in this program will keep asking the user for a character till just 1 character is the value
    user_input = input("Enter a character: ")
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")


main()
