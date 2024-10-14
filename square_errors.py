# This program will impliment the try and exception blocks based on a given code

def square_number():
    # Simple Python program to calculate the square of a number
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("The number entered must be a whole number; please enter a whole number.")
        square_number()


square_number()
