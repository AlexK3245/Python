"""
    This program will get the user's birth month and then generate a calendar
"""

import datetime
import calendar


def main():
    try:
        # Main function of the program where everything is executed
        year = datetime.datetime.now().year
        month = int(input('Enter the month you were born (March would be 3)'))
        print(calendar.month(year, month))
    except ValueError:
        print('Invalid month entered, please enter a number between 1 and 12.')
    except Exception as e:
        print(e)


main()
