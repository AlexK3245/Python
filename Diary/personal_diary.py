# This assignment will take the users input and put it into a diary

def main():
    # This function is the main function where it will prompt the user for the info it is looking for
    date = input("Enter the current date (format MM/DD/YY): ")
    time = input("Enter the current time: ")
    entry = input("Please enter your diary entry: ")

    # Open or create the file in write mode
    with open('Diary/diary.txt', 'a') as file:
        file.write(date + ', ' + time + "\n" + entry + "\n\n")


main()
