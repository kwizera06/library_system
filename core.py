from .utils import track_access, permission_check

class Book:
    

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author


class Library:
    

    def __init__(self):
        self._books = []

    def __getitem__(self, index):
        return self._books[index]

    def __len__(self):
        return len(self._books)

    @permission_check("Admin")
    def add_book(self, user, book: Book):
        self._books.append(book)
        print(f"Book added: {book}")

    @track_access
    def borrow_book(self, user, title: str):
        for book in self._books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"{user.name} borrowed '{book.title}'")
                return
        print("Book not available.")
    
    @track_access
    def return_book(self, user, title: str):
        for book in self._books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"{user.name} returned '{book.title}'")
                return
        print("Book not found or already returned.")
