# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute for availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Readable representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out."
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' not found in the library."

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' has been returned."
                else:
                    return f"'{title}' was not checked out."
        return f"'{title}' not found in the library."

    def list_available_books(self):
        """List all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")

