# Define the Book class
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    # Method to display book information
    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

    # Method to mark the book as borrowed
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You've successfully borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently borrowed.")

    # Method to return the book
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You've successfully returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

# Define the Library class
class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list to store Book objects

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    # Method to list all available books
    def list_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.available:
                book.display_info()

    # Method to borrow a book by title
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print(f"Book '{title}' not found in the library.")

    # Method to return a book by title
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")

# Step 3: Adding a user interface with a menu for interacting with the library
def library_menu():
    library = Library()
    
    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. List Available Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book = Book(title, author)
            library.add_book(book)
        
        elif choice == '2':
            library.list_available_books()
        
        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        
        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        
        elif choice == '5':
            print("Exiting the library system.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the library menu
library_menu()
