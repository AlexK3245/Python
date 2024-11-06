"""
    This assignment will ask the user for a password and then check to see if it meets all criteria
"""


def main():
    valid = False
    while not valid:
        valid = True
        print("""Password Requirements:\n
            Between 8 to 20 characters long.\n
            Contains at least one uppercase letter.\n
            Contains at least one lowercase letter.\n
            Includes at least one number.\n
            Includes at least one symbol from the set: !@#$%&*.\n""")

        password = input("Enter a password (must meet all criteria): ")
        length = len(password)
        if 8 < length < 20:
            continue
        else:
            valid = False
            print("That password is not the right length")

        is_upper = False
        for char in password:
            if char.isupper():
                is_upper = True
        if is_upper == False:
            valid = False
            print("Password must contain at least 1 uppercase letter")

        is_lower = False
        for letter in password:
            if letter.islower():
                is_lower = True
        if is_lower == False:
            valid = False
            print("Password must contain at least 1 lowercase letter")

        has_number = False
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        for n in number:
            for b in password:
                if n == b:
                    has_number == True
        if has_number == False:
            print("Please make sure to include a number.")
            valid = False

        has_symbol = False
        symbol = ['!', '@', '#', '$', '%', '&', '*']
        for s in symbol:
            for c in password:
                if s == c:
                    has_symbol == True
        if has_symbol == False:
            print("You need to include a symbol")
            valid = False
            continue
    password_2 = input("Please re-enter your password: ")
    if password == password_2:
        print("Successful!")
    else:
        print("Passwords did not match, please restart.")
        main()


main()
