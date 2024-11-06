"""
    _summary_
    (I looked up on google how to easily remove the last item in a list and it gave me the pop() method)
"""


def main():
    # This function serves as the main function for the program where everything is put into
    try:
        flowers = []
        flower = 0
        number = 1
        while flower != "done":
            flower = input("Enter the name of a flower: ")
            flowers.append(flower)
        flowers.pop()  # removing 'done' from list
        # Should we change them all to the same case first????
        flowers = sorted(flowers)
        print(flowers)
        for flower in flowers:
            print(number, flower)
            number = number + 1

        search = int(
            input("Please enter the number of the flower you want to search for: "))
        print(f"The flower you are looking for is: {
            flowers[search - 1]}")
    except ValueError:
        print("Please make sure you are entering a positive number.")
        main()
    except IndexError:
        print("Please make sure you are entering a positive number")
        main()
    except:
        print("Please make sure you are following the instructions.")
        main()


main()
