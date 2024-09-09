# Decisions assignment

"""
Write a Python program that uses if else statements and:

Ask the user for their age.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount (65).
Print all the results on the screen.

"""

age = float(input("How old are you? "))

if age >= 15:
    print("\nYou are old enough to drive.")
else:
    print("\nYou are not old enough to drive.")

if age >= 18:
    print("You can vote.")
else:
    print("You can't vote.")

if age >= 21:
    print("You can buy alcohol legally.")
else:
    print("You can't buy alcohol legally.")

if age >= 65:
    print("You are eligible for the senior discount.\n")
else:
    print("You are not eligible for the senior discount.\n")
