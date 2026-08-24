from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    @abstractmethod
    def calcular_ipva(self):
        pass

class Carro(Veiculo):
    def __init__(self,  marca, modelo, ano, valor, cavalos):
        super().__init__(marca, modelo, ano, valor)
        self.cavalos = cavalos

    def calcular_ipva(self):
        return self.valor*0.04

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, valor, cilindrada):
        super().__init__(marca, modelo, ano, valor)
        self.cilindrada = cilindrada

    def calcular_ipva(self):
        return self.valor*0.02

carro1 = Carro("Vw", "Polo", 2024, 50000, 150)
moto1 = Moto("Honda", "Sahara", 2023, 50000, 300)

print(carro1.calcular_ipva())
print(moto1.calcular_ipva())