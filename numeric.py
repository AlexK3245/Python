# Define a custom exception
class NotNumericError(Exception):
    def __init__(self, number, message="Number is not valid"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    # Getter and Setter for pet_kind
    def get_number(self):
        return self.__number

    def get_message(self):
        return self.__message

    def set_number(self, value):
        self.__number = value

    def set_message(self, value):
        self.__message = value

    def __str__(self):
        return f"{self.number} --> {self.message}"


# Usage of the custom exception
def main():
    # This function will run the program
    try:
        number = input("Enter a number: ")
        if number.isnumeric():
            print(number)
        else:
            raise NotNumericError("Custom error occurred")
    except NotNumericError as e:
        print(f"Caught an error: {e.message}")
    else:
        print("No errors have occured")
    finally:
        print("Your Number has been saved")


main()
