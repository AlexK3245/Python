# This program will take a song and convert it into a mad lib

# This function will print the first two stanzas of the song "It's beginning to look a lot like Christmas" but as a mad lib
def custom_song(holiday, verb, verb_2, verb_3, noun, noun_2, noun_3, adjective):
    print("\n\n")
    print(f"It's beginning to look a lot like {holiday}")
    print(f"Everywhere you {verb}")
    print(f"Take a {verb_2} at the five and ten, {verb_3} once again")
    print(f"With candy {noun} and silver {noun_2} aglow.")
    print("\n")
    print(f"It's beginning to look a lot like {holiday}")
    print(f"{noun_3} in every store")
    print(f"But the {adjective} sight to see is the holly that will be")
    print("On your own front door.")


# These variables will gather the different words being added by the user to use for the mad lib
input_holiday = input("Enter a holiday: ")
input_verb = input("Enter a verb: ")
input_verb_2 = input("Enter another verb: ")
input_verb_3 = input("Enter a verb ending in ING: ")
input_noun = input("Enter a noun - Plural: ")
input_noun_2 = input("Enter another noun - Plural: ")
input_noun_3 = input("Enter another noun - Plural: ")
input_adjective = input("Enter an adjective - ends in EST: ")

custom_song(holiday=input_holiday, verb=input_verb,
            verb_2=input_verb_2, verb_3=input_verb_3, noun=input_noun,
            noun_2=input_noun_2, noun_3=input_noun_3, adjective=input_adjective)
