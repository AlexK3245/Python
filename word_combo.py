def two_letter_combinations(characters):
    # Implement the generator function
    # This will allow it to iterate through the list of characters and will combine them
    for letter in characters:
        for my_letter in characters:
            yield letter + my_letter


def main():
    # Call the generator function and print each combination
    characters = ["a", "l", "e", "x", "k"]
    result = list(two_letter_combinations(characters))
    result.sort()
    print(result)


main()
