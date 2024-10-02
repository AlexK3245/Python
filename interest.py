# This program will calculate simple interest while also returning a result

principal = int(input("What is your initial sum of money? "))
rate = int(input("What is your rate of interest (as a percent)? "))
time = int(input(
    "How long has your money been invested or borrowed for, in years? "))


def calculate_interest(principal, rate, time):
    # This function will calculate the interest and store it in return
    calculated_interest = (principal * rate * time) / 100
    return calculated_interest


calculated_interest = calculate_interest(principal, rate, time)
print(f"The simple interest for a principal amount of ${principal:,.2f} at an interest rate of {
      rate}% over a period of {time} years is: ${calculated_interest:,.2f}")
