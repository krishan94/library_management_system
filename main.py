from add_books import Add_Book
from show_books import Show_Books
from issue_book import Issue_Books
from return_book import Return_Books



def library():
    print("\nWelcome To The Library")
    while True:
        print("\n1. Add Book")
        print("\n2. Show Book")
        print("\n3. Issue Book")
        print("\n4. Return Book")
        print("\n5. Exit")

        choice = int(input("\nEnter The Choice: "))

        if choice == 1:
            Add_Book()
        elif choice == 2:
            Show_Books()
        elif choice == 3:
            Issue_Books()
        elif choice == 4:
            Return_Books()
        elif choice == 5:
            print("\nThank you!")
            break
        else:
            print("Invalid choice")
            break
library()