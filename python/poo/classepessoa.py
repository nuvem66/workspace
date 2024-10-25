#What year is it?
currentyear = input("What year is it? ")
#creating class product

class Person: #inicial maiúscula, geralmente no singular e substantivo 
    def __init__(self, name, birthyear, cpf, height, weight) -> None: 
         
        self.name = name
        self.birthyear = birthyear
        self.cpf = cpf
        self.height = height
        self.weight = weight
        #armazena o atributo 'nome' da própria função na variável 'nome'
    def calcAge(self, years):
        newage = currentyear - self.birthyear
        
    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {currentyear - self.birthyear}\nCPF: {self.cpf}\nHeight: {self.height}\nWeight: {self.weight}" #'{something}' insere algo na string
        #'f' it's a formatter: it returns a string like 'name - price'

p1 = Person("zack", 2003, 19499998750, 186.4, 65.3)
print(p1)
    
    