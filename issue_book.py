from Utils import Books, Issued_Books,Issued_date
from datetime import date

def Issue_Books():
    if len(Books) == 0:
        print("No Book Available")
    book_name=input("\nEnter the name of the book you want to issue: ").title()
    if book_name in Books:
        Books.remove(book_name)
        Issued_Books.append(book_name)
        date1 = date.today()
        Issued_date.update({book_name:date1})
        

        print(f'\nBook {book_name} successfully issued on date:',date1)
        print(f"Return by within 14 days")
    else:
        print(f'\n {book_name} is not available in the  library.')
        Issue_Books()