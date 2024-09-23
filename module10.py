# Step 1: Create the Book class
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"'{self.title}' by {self.author} - {availability}"

# Step 2: Create the Library class to manage the collection of books
class Library:
    def __init__(self):
        self.books = []

    # Method to add a book
    def add_book(self, book):
        self.books.append(book)

    # Method to search for books by title using a lambda function
    def search_by_title(self, title):
        result = list(filter(lambda book: title.lower() in book.title.lower(), self.books))
        return result

    # Method to search for books by author using a lambda function
    def search_by_author(self, author):
        result = list(filter(lambda book: author.lower() in book.author.lower(), self.books))
        return result

    # Method to update book availability using a lambda function
    def update_availability(self, title, availability):
        updated = False
        # Find the book and update availability
        self.books = list(map(lambda book: Book(book.title, book.author,
                                                availability) if book.title.lower() == title.lower() else book,
                              self.books))
        # Check if the update happened
        updated = any(book.title.lower() == title.lower() for book in self.books)
        return updated


# Step 3: Test the functionality
def test_library():
    # Create a library instance
    library = Library()

    # Create some books
    book1 = Book("The Psychology of Money", "Morgan Housel")
    book2 = Book("The Brain The Story of You", "David Eagleman")
    book3 = Book("The Code Breaker", "Jennifer Doudna", available=False)

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Search for books by title
    print("\nSearch by title 'The Psychology of Money':")
    for book in library.search_by_title("The Psychology of Money"):
        print(book)

    # Search for books by author
    print("\nSearch by author 'Morgan Housel':")
    for book in library.search_by_author("Morgan Housel"):
        print(book)

    # Update availability of a book
    print("\nUpdating availability of 'The Great Gatsby' to Not Available...")
    library.update_availability("The Great Gatsby", False)

    # Show the updated availability
    print("\nLibrary Inventory after updating availability:")
    for book in library.books:
        print(book)

# Run the test
test_library()
