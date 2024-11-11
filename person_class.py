# Class definition for a Person
class Person:
    # Initializer with private variables
    def __init__(self, name, address, age, phone):
        self.__name = name  # Private variable for name
        self.__address = address    # Private variable for address
        self.__age = age    # Private variable age
        self.__phone = phone   # Private variable for phone number

    # Method to get person's info as a formatted string
    def get_info(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, #: {self.__phone}"

    # Getter for name
    def get_name(self):
        return self.__name

    # Getter for address
    def get_address(self):
        return self.__address

    # Getter for age
    def get_age(self):
        return self.__age

    # Getter for phone number
    def get_phone(self):
        return self.__phone

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Setter for address
    def set_address(self, address):
        self.__address = address

    # Setter for age
    def set_age(self, age):
        self.__age = age

    # Setter for phone
    def set_phone(self, phone):
        self.__phone = phone


def main():
    # Main function for the program to run everything
    person_1 = Person("Alex", "123 Great St", "19", "224-278-9276")
    person_2 = Person("Aiden", "3263 Awesome St", "21", "224-436-4712")
    person_3 = Person("Hunter", "1039 Good St", "25", "847-346-1257")

    print(person_1.get_info())
    print(person_2.get_info())
    print(person_3.get_info())


main()
