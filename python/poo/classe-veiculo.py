class Veiculo: 
    def __init__(self, marca, modelo, ano) -> None: 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def descreva(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}"
    def combustivel(self):
        pass
    def extras(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    def combustivel(self):
        return f"Gasolina"
    def extras(self):
        return f"{self.portas} portas"
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    def combustivel(self):
        return f"Gasolina"
    def extras(self):
        return f"{self.cilindradas} cilindradas"
    
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima
    def combustivel(self):
        return f"Diesel"
    def extras(self):
        return f"{self.carga_maxima} carga"

honda = Moto("honda", "pop16", 2010, 16)

def mostre(objeto):
    print(f"{objeto.descreva()} - Tipo de combustível: {objeto.combustivel()} - {objeto.extras()}")

mostre(honda)