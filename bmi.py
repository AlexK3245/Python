# This assignment will calculate a persons BMI and then tell them whether it is normal or not

# Global variable declaration
CONVERSION_WEIGHT = 0.453592
CONVERSION_HEIGHT = 0.0254


def calculate_bmi(get_weight, get_height):
    # This function will calculate the conversions of weight and height from the
    # user and then calculate the bmi and return that value. This will also determine what category the person is in
    weight = get_weight * CONVERSION_WEIGHT
    height = get_height * CONVERSION_HEIGHT
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("You are in the underweight category")
    elif bmi >= 18.5 and bmi < 24.9:
        print("You are in the Normal weight category")
    elif bmi >= 25 and bmi < 29.9:
        print("You are in the overweight category")
    elif bmi >= 30:
        print("You are in the obese category")
    return bmi


# Input from the user
get_weight = int(input("Enter your weight in pounds (whole number): "))
get_height = int(input("Enter your height in inches (whole number): "))

print(f"Your BMI is: {calculate_bmi(get_weight, get_height):.2f}")
