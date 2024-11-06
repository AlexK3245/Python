def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    try:
        index_num = int(input("Enter the index of the artist to replace: "))
        new_artist = input("Enter the new artist name: ")
        top_artists[index_num] =
        print(top_artists)
        top_artists.append(index_num, new_artist)
        print(f"Updated list: {top_artists}")
    except ValueError:
        print("Please make sure you are entering a valid integer.")
        main()
    except IndexError:
        print("Please make sure you are entering a valid index between 0 and 9")
        main()
    except:
        print("Please make sure you are following all of the instructions.")
        main()


main()
