from .core import Book, Library
from .utils import User


def main():
    admin = User("Prince", "Admin")
    member = User("Sano", "Member")

    library = Library()

    
    library.add_book(admin, Book("1984", "George Orwell", 200))
    library.add_book(admin, Book("The Hobbit", "J.R.R. Tolkien", 201))

    print("\n--- Library Collection ---")
    for book in library:
        print(book)

    print("\n--- Borrow / Return ---")
    library.borrow_book(member, "1984")
    library.return_book(member, "1984")

    print("\n--- Magic Methods Demo ---")
    book1 = Book("Clean Code", "Robert C. Martin", 300)
    book2 = Book("Clean Code", "Robert C. Martin", 301)

    print(book1)
    print("Pages:", len(book1))
    print("Books equal?", book1 == book2)


if __name__ == "__main__":
    main()
