
while True:

    class Veiculo:
        def __init__(self, marca, modelo, ano, valor):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
            self.valor = valor

    class Carro(Veiculo):
        def calcular_ipva(self):
            return self.valor * 0.04

    class Moto(Veiculo):
        def calcular_ipva(self):
            return self.valor * 0.02

    '''carro1 = Carro(marca="VW", modelo="Polo GTS", ano=2024, valor=124000)
    print(f"Marca:{carro1.marca}  Modelo:{carro1.modelo}  Ano:{carro1.ano}  Valor:{carro1.valor}  IPVA:{carro1.calcular_ipva()}")

    moto1 = Moto(marca="Honda", modelo="Bis", ano=2024, valor=16000)
    print(f"Marca:{moto1.marca}  Modelo:{moto1.modelo}  Ano:{moto1.ano}  Valor:{moto1.valor}  IPVA:{moto1.calcular_ipva()}")'''

    x = input("Deseja cadastrar algum veículo? [S/N]:")
    if x == "S":
        print("MENU")
        print()
        ma = input("Marca: ")
        mo = input("Modelo: ")
        an = int(input("Ano: "))
        va = int(input("Valor: "))

        carro2 = Carro(marca=ma, modelo=mo, ano=an, valor=va)
        print(f"Marca:{carro2.marca}  Modelo:{carro2.modelo}  Ano:{carro2.ano}  Valor:{carro2.valor}  IPVA:{carro2.calcular_ipva()}")
    else:
        print("Obrigado!")
        break



