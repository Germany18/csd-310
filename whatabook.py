import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def showBooks (cursor) :
    cursor.execute ("select * from book")
    books = cursor.fetchall()
    print()
    for book in books :
        print (book[1])
    print()

def showLocations (cursor) :
    cursor.execute ("select * from store")
    locations = cursor.fetchall()
    print()
    for location in locations :
        print (location[1])
    print()

def validateUser (cursor, id) :
    cursor.execute (f"select * from user where user_id = {id}")
    user_id = cursor.fetchone()
    return user_id

def showWishlist (cursor, user) :
    cursor.execute (f"select book_name, author, details, locale from wishlist w INNER JOIN book b on w.book_id = b.book_id INNER JOIN book_availability ba on ba.book_id = b.book_id INNER JOIN store s on ba.store_id = s.store_id where w.user_id = {user[0]}")
    books = cursor.fetchall()
    print()
    for book in books :
        print (book[0])
    print()

def addBookToWishlist (cursor, user, book) :
    cursor.execute (f"insert into wishlist (book_id, user_id) VALUES ({book[0]}, {user[0]})")


def showBooksToAdd (cursor, user) :
    cursor.execute (f"select b.book_id, book_name, author, details from book b INNER JOIN book_availability ba on ba.book_id = b.book_id where b.book_id not in (select book_id from wishlist where user_id = {user[0]}) and ba.store_id = {user[3]}")
    books = cursor.fetchall()
    index = 1
    print()
    for book in books :
        print (f"{index}. {book[1]}, {book[2]}")
        index = index + 1   
    print()
    return books

def showAccountMenu (cursor, user) :
    finished = False
    while not finished :
        print ("1. Wishlist")
        print ("2. Add book")
        print ("3. Main Menu")
        print()
        choice = input ("Please make a selection ")
        if choice == "1" :
            showWishlist(cursor, user)
        elif choice == "2" :
            books = showBooksToAdd(cursor, user)
            bookChoice = int (input ("Please select a book "))
            if bookChoice > 0 and bookChoice <= len(books) :
                book = books [bookChoice -1]
                addBookToWishlist (cursor, user, book)
        elif choice == "3" :
            finished = True 
        else :
            print ()
            print (f"{choice} was not an option")
            print ()

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    finished = False
    while not finished :
        print ("1. View Books")
        print ("2. View Store Locations")
        print ("3. My Account")
        print ("4. Exit Program")
        print ()
        choice = input ("Please make a selection ")
        if choice == "1" :
            showBooks(cursor)
        elif choice == "2" :
            showLocations(cursor)
        elif choice == "3" :
            userChoice = input ("Please provide user ID ")
            user = validateUser (cursor, userChoice)
            if user != None :
                showAccountMenu (cursor, user)
        elif choice =="4" :
            finished = True
        else :
            print ()
            print (f"{choice} was not an option")
            print ()
    db.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)