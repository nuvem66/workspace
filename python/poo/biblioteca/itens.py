itemID = 0
itemList = []
currentlyBorrowed = []

userID = 0
userList = []

def showItens():
    for item in itemList:
        print(item)

def genItemID(title, author, avaliable):
    global itemID
    currentID = itemID

    itemList.append({
        "id": currentID,
        "title": title,
        "author": author,
        "avaliable": avaliable
        })
    
    itemID += 1
    return currentID

def genUserID(name, age, isAdmin):
    global userID
    currentID = userID

    userList.append({
        "id": currentID,
        "isAdmin": isAdmin,
        "name": name,
        "age": age
    })

    userID += 1
    return currentID

class LibraryItem():
    def __init__(self, title, author, avaliable = True) -> None:
        self.title = title
        self.author = author
        self.avaliable = avaliable

class Book(LibraryItem):
    def __init__(self, title, author, avaliable=True) -> None:
        super().__init__(title, author, avaliable)
        self.id = genItemID(self.title, self.author, self.avaliable)

    def borrow(self):
        itemList[self.id]["avaliable"] = False
        currentlyBorrowed.append(itemList[self.id])
    
    def unborrow(self):
        itemList[self.id]["avaliable"] = True
        currentlyBorrowed.remove(itemList[self.id])

narnia = Book("asdab", "eu")
narnia_dois = Book("asda443223b", "eu3")
narnia_quatro = Book("asdasdasdasdab", "eu2")

class User:
    def __init__(self, name, age, isAdmin = False) -> None:
        self.name = name
        self.age = age
        self.isAdmin = isAdmin
        self.borrowList = []
    
class UserAdmin(User):
    def __init__(self, name, age, isAdmin=True) -> None:
        super().__init__(name, age, isAdmin)
        self.id = genUserID(self.name, self.age, self.isAdmin)
        
    def borrow(user, book):
        if itemList[book.id]["avaliable"] == False or len(user.borrowList) >= 3:
            print("Erro: usuário ultrapassou o limite de empréstimos ou o livro não está disponível no momento.")
        else:
            book.borrow()
            user.borrowList.append(book)


narnia.borrow()

