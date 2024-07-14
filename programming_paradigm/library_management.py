class Book:
    """A class representing a book in a library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out
    
class Library:
    """A class representing a library."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return 
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"'{title}' not found in the library.")        

    def list_available_books(self):
        """List available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")    
        