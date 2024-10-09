# This program will take a tuple that has classes inside of it and then print them

def main():
    # This function will use the tuple defines and then print each thing in the tuple and then say how many things total there is in the tuple
    programming_classes = ("Intro to python", "Advanced Python", "Database Essentials",
                           "Web Development Basics", "Data Structures in Python", "Web Design Fundementals")
    for classes in programming_classes:
        print(classes)
    length = len(programming_classes)
    print(f"There are {length} different types of programming classes at MCC")


main()
