# This program will get 2 numbers from the user and then compare those numbers

num_1 = int(input("Enter an integer: "))
num_2 = int(input("Enter another integer: "))

# This will determine whether both numbers are greater than 0 or not
if num_1 > 0 and num_2 > 0:
    print("Both numbers are greater than 0: True")
else:
    print("Both numbers are greater than 0: False")

# This will determine whether or not both numbers are greater than 50
if num_1 > 50 and num_2 > 50:
    print("Both numbers are greater than 50: True")
else:
    print("Both numbers are greater than 50: False")

# This will determine whether either number is negative
if num_1 < 0 or num_2 < 0:
    print("Either number is less than 0: True")
else:
    print("Either number is less than 0: False")

# This will determine whether either number is odd
if num_1 % 2 == 1 or num_2 % 2 == 1:
    print("Either number is odd: True")
else:
    print("Either number is odd: False")

# This will determine whether the numbers equal each other
if not num_1 == num_2:
    print("Each number is unique: True")
else:
    print("Each number is unique: False")

# This will determine whether the second number is greater than 20
if not num_2 > 20:
    print("num_2 is not greater than 20: True")
else:
    print("num_2 is not greater than 20: False")
