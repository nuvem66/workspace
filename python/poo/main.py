
#creating class product
class Product: #inicial maiúscula, geralmente no singular e substantivo 
    def __init__(self, name, price, qnt) -> None: 
        #'def' creates a function 
        #'__init__' it's a builder function
        self.name = name 
        #armazena o atributo 'nome' da própria função na variável 'nome'
        self.price = price
        self.qnt = qnt
    def __str__(self) -> str:
        return f"Product: {self.name}.\nPrice: {self.price}. {self.qnt} remaining." #'{something}' insere algo na string
        #'f' it's a formatter: it returns a string like 'name - price'
    def updateprice(self, newprice):
        self.price = newprice
        print(f"{self.name}'s was changed to {self.price}.")
    
    def selled(self, numberofsells): #adding a method to change sells
        remaining = self.qnt - numberofsells
        self.qnt = remaining


#creating an instance of product
p1 = Product("laptop",1000,5)
print(p1)

p1.selled(4)
print(f"Updated: {p1}")
