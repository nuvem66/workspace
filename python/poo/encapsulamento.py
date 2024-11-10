# 1. Como a herança facilitouu a crialção da classe Gerente?
# A herança, principalmente, reduz bastante a quantidade de código que tenho de escrever.
# Além disso, na minha cabeça, é criado um senso de relação entre os objetos e classes.

# 2. Como o encapsulamento protegeu o acesso direto ao salário?
# Acho que a proteção que o encapsulamento gerou nesse caso, foi a impossibilidade de
# aparente de acessar self.salary diretamente.
 
# 3. O que mudaria no código se o salário fosse acessível diretamente?
# self._salary -> self.salary. Em termos práticos, o atributo salário passaria a ser um 
# atributo publicamente acessável, podendo gerar problemas de privacidade e segurança.

# Encapsulamento
class Employee:
    def __init__(self, name, position, salary = 0):
        self.name = name
        self.position = position
        self._salary = salary
    
    # Descritivas
    def __str__(self) -> str:
        return f'Name: {self.name}\nPositition: {self.position}\n'
    
    def showSalary(self) -> str:
        return f'Salary: R${self._salary:.2f}\n'

    # Outros métodos
    def increaseSalary(self, value):
        if not value > 0:
            print("Error: salary can't be decreased or increase value can't be 0.\n")
        else:
            old_salary =  self._salary
            self._salary += value
            print(f"Salary increased with success.\nNew salary: R${self._salary:.2f}. Salary increased {(self._salary - old_salary)/old_salary * 100:.2f}%\n")

# Instanciação
class Manager(Employee):
    def __init__(self, name, position, salary = 0, bonus = 1.25) -> None:
        super().__init__(name, position, salary)
        self._bonus = bonus
        self._salary *= self._bonus

    def changeBonus(self, value):
        if value < 1:
            print("Error: bonus can't be lesser than 1.\n")
        else:
            self._bonus = value
            self._salary *= self._bonus
            print("Bonus changed with success.\n")

Joao = Employee('Joao', 'Arquiteto', 10000)
print(Joao, Joao.showSalary())
# O uso da vírgula gera o espaço antes de salário. É a vida!

Joao.increaseSalary(2000)
print(Joao, Joao.showSalary())

Bob = Manager('Bob', 'Arquiteto', 10000)
print(Bob, Bob.showSalary())

Bob.increaseSalary(340)
print(Bob, Bob.showSalary())

Bob.changeBonus(1.5)
print(Bob.showSalary())