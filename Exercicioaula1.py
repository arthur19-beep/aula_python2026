class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar(self, numero):
        self.quantidade += numero
        print(f"Agora você tem {self.quantidade} {self.nome}s")

    def remover(self, numero):
        self.quantidade -= numero
        print(f"Agora você tem {self.quantidade} {self.nome}s")

    def calcular(self):
        total = (self.preco * self.quantidade)
        print(f"O valor total é de {total} reais em {self.nome}s")

    def info(self):
        print(f"Produto:{self.nome}")
        print(f"Preço:{self.preco} reais")
        print(f"Quantidade:{self.quantidade} unidades")
        print(f"Total:{self.quantidade * self.preco} reais")


fone = Produto("Fone de ouvido", 19.90, 10)
print()
print()
fone.adicionar(10)
print()
fone.remover(5)
print()
fone.calcular()
print()
fone.info()
print()
print()

bicicleta = Produto("Bicicleta", 399.90, 30)
print()
print()
bicicleta.adicionar(30)
print()
bicicleta.remover(10)
print()
bicicleta.calcular()
print()
bicicleta.info()
