class Contabancaria: #inicial maiúscula, geralmente no singular e substantivo 
    def __init__(self, cliente, saldo) -> None:
        self.cliente = cliente
        self.saldo = saldo 
        
    def __str__(self) -> str:
        return f"Titular: {self.cliente}\nSaldo: R${self.saldo:.2f}\n" 
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"deposito de {valor} realizado com sucesso")
        else:
            print(f"{valor} é um depósito inválido.")

    def saque(self, valor):
        if valor > self.saldo or valor <= 0:
            print(f"{valor} é um depósito inválido.")
        else:
            self.saldo -= valor
            print(f"valor {valor} sacado com sucesso \nsaldo restante: {self.saldo}") 

karol = Contabancaria("karol", 1000)
print(karol)

karol.deposito(136)

print(karol)

karol.saque(0)
print(karol)
