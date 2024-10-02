# Initialize a list of names
names = []

# Ask user for 5 names
for i in range(1, 6):
    names.append(input("Type a name: "))


# Flag to track if a swap has occurred
swapped = True

# put all names in acsending order
names.sort()

# Continue looping until no swaps occur
while swapped:
    swapped = False  # Reset the flag at the start of each iteration
    for i in range(len(names) - 1):
        # Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print(names)

# Reverse the list
names.reverse()

# Print the reversed list
print(names)
