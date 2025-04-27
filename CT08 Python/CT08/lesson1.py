'''
Debugging - Library Program
A library program needs to keep track of books being borrowed and returned. 
Each book has a unique ID and a title. The program allows a user to 
input the book ID and whether the book is being borrowed or returned. 
The program updates the status of the book accordingly and displays a message. 
There are several syntax and logic errors in the program.
'''
### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

if action == "b":
    if books[book_id] == "AVAILABLE":
        books[book_id] == "BORROWED"
        print(books)
        print("You have borrowed the book.")
    else:
        print(books)
        print("The book is already borrowed.")
elif action == "r":
    if books[book_id] == "BORROWED":
        books[book_id] == "AVAILABLE"
        print(books)
        print("You have returned the book.")
    elif books[book_id] == "AVAILABLE":
        print(books)
        print("The book is already AVAILABLE.")
else:
    print(books)
        print("Invalid action.")

'''
Identify and correct the errors in the program so that it works according to 
the requirements given. Save your program.
'''