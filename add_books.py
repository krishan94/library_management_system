from Utils import Books

def Add_Book():
    book_name=input("\nEnter the name of the book: ").title()
    Books.append(book_name)
    print(f'\nBook {book_name} is added successfully!')
    

