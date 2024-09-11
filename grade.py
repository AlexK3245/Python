# Elif assignment
"""
    Accept a numeric grade from the user and display a letter grade. 
    The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, 
    Below 60: F 
    Check to see if the number given is between 0 and 100.  
"""

grade = int(input("\nEnter the numeric grade: "))

if grade >= 90:
    print("The letter grade is: A\n")
elif grade >= 80:
    print("The letter grade is: B\n")
elif grade >= 70:
    print("The letter grade is: C\n")
elif grade >= 60:
    print("The letter grade is: D\n")
else:
    print("The letter grade is: F\n")
