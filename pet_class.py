# Class definition
class Pet:
    # Class variable
    vet_name = "Dog Health"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and Setter for owner_first_name
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    # Method to print pet details
    def print_pet_details(self):
        print("Pet Details:", vars(self))

    # Method to print basic info about the pet
    def print_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)


# Function used to check to verify if the property exists

def check_property():
    pet_1 = Pet("Alex", "Kasper", '3245', "Charlie", "Bichon shih tzu")
    print(hasattr(pet_1, "_Pet__owner_first_name"))
    print(hasattr(pet_1, "_Pet__owner_last_name"))
    print(hasattr(pet_1, "_Pet__pet_id"))
    print(hasattr(pet_1, "_Pet__pet_name"))
    print(hasattr(pet_1, "_Pet__pet_type"))


# Main function to demonstrate usage of the Pet class

def main():
    # Creating an instance of Pet
    pet_1 = Pet("Alex", "Kasper", '3245', "Charlie", "Bichon shih tzu")

    check_property()

    print("\n")
    print(pet_1.get_owner_first_name())
    pet_1.print_pet_details()
    pet_1.print_info()

    print("\n")
    pet_1.set_pet_type("Dog")
    pet_1.print_info()

    pet_2 = Pet("Anthony", "Bieri", '5872', "Bruno", "French Bull Dog")

    print("\n")
    check_property()

    print("\n")
    print(pet_2.get_owner_first_name())
    pet_2.print_pet_details()
    pet_2.print_info()

    print("\n")
    pet_2.set_pet_type("Dog")
    pet_2.print_info()

    pet_3 = Pet("Aiden", "Saez", '2537', "Amber", "American Foxhound")

    print("\n")
    check_property()

    print("\n")
    print(pet_1.get_owner_first_name())
    pet_3.print_pet_details()
    pet_3.print_info()

    print("\n")
    pet_3.set_pet_type("Dog")
    pet_3.print_info()


# Calling the main function
main()
