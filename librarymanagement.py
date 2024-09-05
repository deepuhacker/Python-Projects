class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f'Book "{book.title}" removed from the library.')
                return
        print("Book not found.")

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.copies > 0:
                    book.copies -= 1
                    print(f'Book "{book.title}" lent out.')
                else:
                    print(f'Sorry, all copies of "{book.title}" are currently lent out.')
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.copies += 1
                print(f'Book "{book.title}" returned.')
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books:
            print(book)

class LibraryManagementSystem:
    def __init__(self):
        self.library = Library()

    def show_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.lend_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                self.library.display_books()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        copies = int(input("Enter number of copies: "))
        book = Book(title, author, isbn, copies)
        self.library.add_book(book)

    def remove_book(self):
        isbn = input("Enter book ISBN to remove: ")
        self.library.remove_book(isbn)

    def lend_book(self):
        isbn = input("Enter book ISBN to lend: ")
        self.library.lend_book(isbn)

    def return_book(self):
        isbn = input("Enter book ISBN to return: ")
        self.library.return_book(isbn)

if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()
