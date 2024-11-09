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
        if value > 0:
            self._salary += value
            return f"Success. +{value}."
        else:
            return f"Failure. {value} <= 0."
        
    def decrease(self, value):
        if value > 0 and value <= self._salary:
            self._salary -= value
            return f"Success. -{value}."
        else: 
            return f"Failure.  {value} <= 0 or {value} > salary."

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

Joao.decrease(700)
print(Joao, '\n')

Bob = Manager('Bob', 'Arquiteto', 10000)
print(Bob, '\n')