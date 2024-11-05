# Encapsulamento
class Employee:
    def __init__(self, name, position, salary = 0):
        self.name = name
        self.position = position
        self._salary = salary
    def __str__(self) -> str:
        return f'Name: {self.name}\nPositition: {self.position}\nSalary: {self._salary}'
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

Joao = Employee('Joao', 'Arquiteto', 5200)
print(Joao, '\n')

Joao.increase(2000)
print(Joao, '\n')

Joao.decrease(700)
print(Joao, '\n')