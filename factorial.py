# This assignment will calculate a facotrial of a number

def factorial(n):
    # This function caluclates the factorial of a given number n
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    # This function will ask the user for a number and the calculate the factorial based on that number
    n = int(input("Enter a non-negative number: "))
    result = factorial(n)
    print(f"The factorial of {n} is {result}.")


# This calls the main function executing the program
main()
