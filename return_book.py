from Utils import Books, Issued_Books,Issued_date
from datetime import date

def Return_Books(): 
    book_name=input('\nEnter the name of the book you want to return: ').title()
    if book_name in Issued_Books:
        Issued_Books.remove(book_name)
        Books.append(book_name)
        
    else:
        print(f'\nBook {book_name} was not issued book.')
        Return_Books()
    day=int(input("Enter today's date:"))
    month=int(input("Enter the month:"))
    year=int(input("Enter  the year:"))
    date2=date(year,month,day)

    print("Date of return is:",date2)
    diff=date2-Issued_date[book_name]
    days=diff.days
    fine=0
    if (days)>14:
        fine=((days)-14)*5

        print("You returned the book late so you have to pay the FINE of :",fine)
        print(f'Book {book_name} returned successfully!')
    else:
        print("Returned on time, No FINE!")

    