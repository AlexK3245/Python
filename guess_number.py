"""
    This assignment wiil ask the user for a number and will tell them if they got it correct or not.
    If they guess incorrectly it will tell them how far they are from the correct number,
    and will promt the user to keep guessing till they get it correct.
"""
import random


def main():
    # This function asks for a number and says if you guessed it or not and how close you were if you guessed wrong
    try:
        random_number = random.randint(1, 100)
        print(random_number)
        number = -5
        while number != random_number:
            number = int(input("Enter a number 1-100: "))
            if number == random_number:
                print("You have guessed the number!")
            elif abs(random_number - number) <= 5:
                print("Very hot")
            elif abs(random_number - number) <= 15:
                print("Hot")
            elif abs(random_number - number) <= 25:
                print("Cool")
            else:
                print("Cold")
    except ValueError:
        print("The number entered should be a whole number between 1 and 100")


main()
