# List operations assignment

# Seats available at the start
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Displays seats available
print(f"The currently available seats are: {seats}")

# Initializes sold variable
sold = 1

# Sold seats
sold_seats = []

# Ticket purchase process
while sold != 0:
    sold = (int(input(
        "Hello! What seat(s) would you like to buy? And please enter 0 when finished purchasing! ")))

    if sold in seats:
        # remove sold from seats
        seats.remove(sold)
        # append sold to sold_seats
        sold_seats.append(sold)

        # Display - thank you, seat {sold} is yours
        print(f"Thank you, seat(s) {sold} is now yours")
        print(f"The available seats are now {seats}")

    elif sold == 0:
        print("Thank you for your purchase!")

    else:
        print("Sorry, but that seat does not exist or has been sold already. Please pick a seat from the available selection.")
        print(seats)
        sold = (int(input("Hello! What seat(s) would you like to buy? ")))
