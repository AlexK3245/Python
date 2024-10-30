"""
        This assingment will prompt the user for 10 titles of books and then append them to a list.
        Then it will capitalize all of the titles and sort them into a new list and print each title
    """


def main():
    # Main function for the program that takes care of everything needed
    titles = []
    while len(titles) != 10:
        books = input("Please enter a title of a book: ")
        books = books.title()
        titles.append(books)
    my_sorted = sorted(titles)
    for title in my_sorted:
        print(title, end="\n")


main()
