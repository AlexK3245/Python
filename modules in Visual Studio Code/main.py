from math_operations import calculator
from math_operations import geometry


def main():
    result = calculator.add(5, 3)
    print("Addition result:", result)

    result = calculator.subtract(10, 4)
    print("Subtraction result:", result)

    result = geometry.rectangle(3, 6)
    print("Rectangle area result:", result)

    result = geometry.circle(3)
    print("Circle area will result:", result)

    result = geometry.triangle(3, 6)
    print("Triangle area result:", result)


main()
