from Utils import Books

def Show_Books():
    if len(Books)==0:
        print("No book available in the library.")
    else:
        print("Available Books:")
        for book in Books:
            print(book)
            