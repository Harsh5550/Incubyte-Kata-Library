from library import Library

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")
            library._add_book(isbn, title, author, year)
        elif choice == "2":
            isbn = input("Enter ISBN of the book to borrow: ")
            library._borrow_book(isbn)
        elif choice == "3":
            isbn = input("Enter ISBN of the book to return: ")
            library._return_book(isbn)
        elif choice == "4":
            library._view_available_books()
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
