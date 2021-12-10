book_list=[]

def add_book(book:tuple,list:list):
    list.append(book)

def remove_book(book:tuple,list:list):
    list.remove(book)

def list_books(book:tuple,list:list):
    for book in list:
        print(f"Book name : {book[0]}, Book author : {book[1]}")

def control(book:tuple,list:list):
    if book in list:
        return True
    else:
        return False

while 1==1:
    option = input("""
    Please choose an option:
    (1) Add book
    (2) Remove book
    (3) List all books
    (4) Quit    
    """)
    if option == "1":
        book_name        = input("Please enter name of book : ")
        book_author      = input("Please enter author of book : ")
        book             = (book_name,book_author)
        add_book(book,book_list)
        print("Book added...")
        input("Please push enter button to continue : ")

    elif option == "2":
        book_name        = input("Please enter name of book : ")
        book_author      = input("Please enter author of book : ")
        book             = (book_name,book_author)
        remove_book(book,book_list)
        print("Book removed...")
        input("Please push enter button to continue : ")

    elif option == "3":
        list_books(book,book_list)

    elif option == "4":
        break
