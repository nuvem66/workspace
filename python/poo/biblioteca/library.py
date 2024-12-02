def getTitle(obj):
    return obj.title
def getName(obj):
    return obj.name
# there's prob a way of merging those two,
# but me = tired

class Book():
    bookList = []

    def __init__(self, title, author, status = "disponible") -> None:
        self.title = title
        self.status = status
        self.author = author
        Book.bookList.append(self)
        Book.bookList.sort(key=getTitle)

    def changeStatus(self, option):
        self.status = "indisponible" if option == 0 else "disponible"

class User():
    userList = []

    def __init__(self, name, age, isAdmin = False):
        self.name = name
        self.age = age
        self.isAdmin = isAdmin
        self.borrows = []
        User.userList.append(self)
        User.userList.sort(key=getName)

    def borrowBook(self, book):
        if len(self.borrows) >= 3:
            print(f"Error: {self.name} already has 3 books in their borrow list.")
            return
        book.changeStatus(0)
        self.borrows.append(book)
        print(f"{book.title} was borrowed by {self.name}.")

    def unborrowBook(self, book):
        if book not in self.borrows:
            print("Error: you didn't borrow this book yet.")
            return
        book.changeStatus(1)
        self.borrows.remove(book)
        print(f"{book.title} is back to the shelf.")

    def showBorrows(self):
        print(f"Books currently borrowed by {self.name}:")
        if not self.borrows:
            print("There's nothing here.")
            return
        counter = 1
        for book in self.borrows:
            print(f"{counter}) {book.title}")
            counter += 1

class Admin(User):
    def __init__(self, name, age, isAdmin = True):
        super().__init__(name, age, isAdmin)
        self.borrows = []
    
    def _addBook(self, title, author):
        return Book(title, author)

    def _remBook(self, book):
        if book not in Book.bookList:
            print(f'Book "{book}" not found.')
            return
        Book.bookList.remove(book) if input(f'Are you sure you want to remove {book.title}? Type "confirm": ') == "confirm" else print("Aborted.")

    def _showAllBooks(self):
        print(f"\n=========== All books: ===========")

        if not Book.bookList:
            print("There are no books in the library.")
            print(f"==================================\n")
            return
        
        for book in Book.bookList:
            print(f"{book.title} by {book.author}. \n↳ Status: {book.status}")
        print(f"==================================\n")

    def _showAllBorrowedBooks(self):
        print(f"\n====== All borrowed books: ======")
        
        if not Book.bookList:
            print("There are no currently borrowed books.")
            print(f"=================================\n")
            return
        
        for book in Book.bookList:
            if book.status == "indisponible":
                print(f"{book.title} by {book.author}.")
        print(f"=================================\n")

    def _showAllUsers(self):
        print(f"\n=========== All Users: ===========")
        users = User.userList

        if not users:
            print("There are currently no users.")

        for user in users:
            print(f"Name: {user.name}\nAge: {user.age}\nAdmin: {user.isAdmin}")
            user.showBorrows()
            print()
        print(f"==================================\n")

Pedro = Admin("Pedro", 19)
Pedro._showAllBooks()
# Creating some books and users (credits to: chatGPT)

ToKillAMockingbird = Pedro._addBook("To Kill a Mockingbird", "Harper Lee")
NineteenEightyFour = Pedro._addBook("1984", "George Orwell")
TheGreatGatsby = Pedro._addBook("The Great Gatsby", "F. Scott Fitzgerald")
TheCatcherInTheRye = Pedro._addBook("The Catcher in the Rye", "J.D. Salinger")
MobyDick = Pedro._addBook("Moby-Dick", "Herman Melville")
PrideAndPrejudice = Pedro._addBook("Pride and Prejudice", "Jane Austen")
WarAndPeace = Pedro._addBook("War and Peace", "Leo Tolstoy")
TheHobbit = Pedro._addBook("The Hobbit", "J.R.R. Tolkien")
Ulysses = Pedro._addBook("Ulysses", "James Joyce")
TheDivineComedy = Pedro._addBook("The Divine Comedy", "Dante Alighieri")

Pedro._showAllBooks()

Aly = User("Alice", 22)
Bob = User("Bob", 25)
Charlie = User("Charlie", 35)
Diana = User("Diana", 28)
Eve = User("Eve", 22)

Aly.borrowBook(NineteenEightyFour)
Aly.borrowBook(MobyDick)
Aly.borrowBook(WarAndPeace)
Aly.borrowBook(TheDivineComedy)

Pedro._showAllBorrowedBooks()
Pedro._showAllUsers()

Aly.unborrowBook(NineteenEightyFour)
Pedro._showAllBorrowedBooks()