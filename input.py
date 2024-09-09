# Input assignment

"""
    Create a Python application that allows users to input their total
    budget and the amount spent in various categories. The program
    will then calculate and display what percentage of the total budget
    each category represents.
"""

# This section is getting the input from the user on each category

budget = float(input("Enter your budget: $"))
housing = float(input("How much do you spend on housing? $"))
utilities = float(input("How much do you spend on utilities? $"))
groceries = float(input("How much do you spend on groceries? $"))
transportation = float(input("How much do you spend on transportation? $"))
health_care = float(input("How much do you spend on health care? $"))
personal_care = float(input("How much do you spend on personal care? $"))
clothing = float(input("How much do you spend on clothing? $"))
debt = float(input("How much debt do you already have? $"))

# This section is going to calculate the percent of the budget that each category is

housing_percent = (housing/budget) * 100
utilities_percent = (utilities/budget) * 100
groceries_percent = (groceries/budget) * 100
transportation_percent = (transportation/budget) * 100
health_care_percent = (health_care/budget) * 100
personal_care_percent = (personal_care/budget) * 100
clothing_percent = (clothing/budget) * 100
debt_percent = (debt/budget) * 100

# This section prints and tells the user the percent that each category is of their budget

print(f"\nYour housing is {housing_percent:.1f}% of your total budget!")
print(f"\nYour utilities are {utilities_percent:.1f}% of your total budget!")
print(f"\nYour groceries are {groceries_percent:.1f}% of your total budget!")
print(f"\nYour transportation is {
      transportation_percent:.1f}% of your total budget!")
print(f"\nYour health care is {
      health_care_percent:.1f}% of your total budget!")
print(f"\nYour personal care is {
      personal_care_percent:.1f}% of your total budget!")
print(f"\nYour clothing is {clothing_percent:.1f}% of your total budget!")
print(f"\nYour debt is {debt_percent:.1f}% of your total budget!\n")
