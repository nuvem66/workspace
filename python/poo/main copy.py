
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
        return f"Product: {self.name}.\nPrice: {self.price:.2f}" #'{something}' insere algo na string
        #'f' it's a formatter: it returns a string like 'name - price'
    
    def idcalc(self):
        nameid = "{self.name}"
        return nameid
    
#creating an instance of product
p1 = Product("laptop",1000,5)

productlist = []

#Trying to manually add a product
def addProduct():
    namen = input("Add a name: ")
    pricen = input("Add a price: ")
    qntn = input("Add a quantity: ")
    productlist.append(Product(namen, pricen, qntn).idcalc)
    print(productlist)

keepRunning = input("Wanna add a new product? Y/N ")

while keepRunning == "y":
    addProduct()
    keepRunning = input("Still wanna add a new product? Y/N ")