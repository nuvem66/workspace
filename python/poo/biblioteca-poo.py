allId = []
lastId = 0

def genId(name, age, object):
    global lastId

    allId.append({
                "name": name,
                "age": age,
                "id": lastId,
                "instance": object
                })
    lastId += 1

class Pessoa():
    def __init__(self, name, age, status = 0):
        self.status = status
        genId(name, age, self)
    def borrowBook(bookId):
        pass

id_0 = Pessoa("Irelia", 24)
id_1 = Pessoa("Karolyne", 25)

for id in allId:
    print(id)