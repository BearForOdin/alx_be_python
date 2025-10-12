class Book:
    def __init__(self, title, author):
        """Base class for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        """Readable representation of a Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Derived class for electronic books."""
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        """Readable representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Derived class for printed books."""
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        """Readable representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library class demonstrating composition — holds multiple books."""
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Lists all books currently in the library."""
        for book in self.books:
            print(book)
