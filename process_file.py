"""
    This program will take in the numbers from another file and then add them all together, 
    average them, and count the number of entries
    
"""


def main():
    # Main function of the program where everything is coded
    try:
        total = 0
        count = 0
        average = 0
        with open('sales_totals.txt', 'r') as file:
            line = file.readline().rstrip("\n")
            while line:
                count = count + 1
                line = float(line)
                total = total + line
                line = file.readline().rstrip("\n")
                print(line)
            average = total / count

        print(f"Total: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {average:,.2f}")

    except IOError:
        print("An IOError has occurred.")


main()
