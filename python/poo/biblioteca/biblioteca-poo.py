all_id = []
last_id = 0

# -> "MyClass":

# Function that will store all ids in AllId
def genId(name, age, borrows):
    global last_id

    all_id.append({
                "name": name,
                "age": age,
                "id": last_id,
                "borrow_list": borrows
                })
    last_id += 1


class Pessoa():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        borrows = []
        self.id = last_id

        genId(self.name, self.age, borrows)

    def borrowBook(bookId):
        pass

Pessoa("Irelia", 24)
Pessoa("Akali", 21)


for id in all_id:
    print(id["name"], id["borrow_list"])