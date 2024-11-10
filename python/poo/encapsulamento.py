# Encapsulamento
class Employee:
    def __init__(self, name, position, salary = 0):
        self.name = name
        self.position = position
        self._salary = salary
    
    # Descritiva
    def __str__(self) -> str:
        return f'Name: {self.name}\nPositition: {self.position}\nSalary: {self._salary}\n'
    
    # Métodos
    def increase(self, value):
        if value < 0:
            return f"Failure. {value} <= 0."
        else:
            self._salary += value
            return f"Success. +{value}."

# Instanciação
class Manager(Employee):
    def __init__(self, name, position, salary = 0, bonus = 1.25) -> None:
        super().__init__(name, position, salary)
        self.bonus = bonus
        self._salary = salary * bonus
    def __str__(self) -> str:
        return f'Name: {self.name}\nPositition: {self.position}\nSalary: {self._salary}\nBonus: {self.bonus}'

Joao = Employee('Joao', 'Arquiteto', 10000)
print(Joao, '\n')

Joao.increase(2000)
print(Joao, '\n')

Bob = Manager('Bob', 'Arquiteto', 10000)
print(Bob, '\n')

Bob.increase(340)
print(Bob, '\n')