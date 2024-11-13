# Class definition
class Pet:
    # Class variable
    vet_name = "Dog Health"

    def __init__(self, pet_kind, pet_breed, pet_name):
        # Instance variables
        self.__pet_kind = pet_kind
        self.__pet_breed = pet_breed
        self.__pet_name = pet_name

    # Getter and Setter for pet_kind
    def get_pet_kind(self):
        return self.__pet_kind

    def get_pet_breed(self):
        return self.__pet_breed

    def get_pet_name(self):
        return self.__pet_name

    def set_pet_kind(self, value):
        self.__pet_kind = value

    def set_pet_breed(self, value):
        self.__pet_breed = value

    def set_pet_name(self, value):
        self.__pet_name = value

    # Method to print pet details
    def print_pet_details(self):
        print("Pet Details:", vars(self))


def main():
    # Main function of the program, will do all of the instances
    pet_1 = Pet("Dog", "Bichon hih tzu", "Charlie")
    pet_1.print_pet_details()
    print(getattr(pet_1, "_Pet__pet_name"))

    pet_2 = Pet("Dog", "French Bulldog", "Bruno")
    pet_2.print_pet_details()
    print(Pet.__name__)

    pet_3 = Pet("Dog", "Bichon hih tzu", "Charlie")
    pet_3.print_pet_details()
    print(isinstance(pet_3, Pet))


main()
