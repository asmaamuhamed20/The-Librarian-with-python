import csv
from typing import List, Dict, Union

# Define the add_book function


def add_book(title: str, authors: List[str], year: int) -> Dict[str, Union[str, List[str], int]]:
    # Create dictionary to represent  the book
    book = {
        "title": title,
        "authors": authors,
        "year": year
    }

   # opening CSV file
    with open("books.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        # add the information of the book like title,author and year  as new row in CSV file
        writer.writerow(
            [book["title"], ", ".join(book["authors"]), book["year"]])

    return book  # return list of book (tile, author , year) 

# Function to add new books to CSV file


def add_new_book():
    try:
        title = input("Hello, Enter the title of the book: ")
        if not title:
            # Error message if the user skipped the title of book
            raise ValueError("Please, Enter a title, Title cannot be empty.")

        authors = input("Enter the authors (comma-separated): ").split(",")
        for author in authors:
            if not author.strip():
                # Error message if the user skipped the author
                raise ValueError("Author names cannot be empty.")

        year = int(input("Enter the year of publication: "))
        if year < 0:
            # Make sure that year is positive integers
            raise ValueError("Year must be a positive integer.")

        book = add_book(title, authors, year)
        # Add new book
        print(f"The book '{book['title']}' has been added successfully!")
    except ValueError as e:
        print(f"Error: {e}")  # Error message if user didn't enter book

# Function to search for a book by title


def search_book(library: List[Dict[str, Union[str, List[str], int]]], title: str) -> Union[Dict[str, Union[str, List[str], int]], None]:
    for book in library:  # Search about is the book found or not
        if book["title"] == title:
            return book  # return book if the book was found
    return None  # return nothing if the book not found

# Function to load books from the CSV file


def load_books():
    library = []  # load book in list
    try:
        with open("books.csv", mode="r") as file:
            reader = csv.DictReader(file)  # read CSV file
            for row in reader:
                authors = row["authors"].split(", ")  # separate authors with comma
                year = int(row["year"])
                book = {
                    "title": row["title"],
                    "authors": authors,
                    "year": year
                }
                library.append(book)  
    except FileNotFoundError:
        # Handle the case where the CSV file doesn't exist, it will return library
        pass
    return library


# while loop tp present the menu of library
while True:
    print("\nOptions:")
    print("1. Add a new book")
    print("2. Search for a book by title")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_new_book()
    elif choice == "2":
        title = input("Enter the title of the book to search for: ")
        library = load_books()
        found_book = search_book(library, title)
        if found_book:
            print("Book found:")
            print(f"Title: {found_book['title']}")
            print(f"Authors: {', '.join(found_book['authors'])}")
            print(f"Year: {found_book['year']}")
        else:
            print(f"No book with title '{title}' found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Thank you,Goodbye!")
