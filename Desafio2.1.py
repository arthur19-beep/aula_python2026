while True:
    class Entrega:
        def __init__(self, distancia, peso):
            self.distancia = distancia
            self.peso = peso

    class EntregaComum(Entrega):
        def calcular_frete(self):
            return self.distancia * 2 + (self.peso * 1)

    class EntregaExpressa(Entrega):
        def calcular_frete(self):
            return self.distancia * 3,5 + (self.peso * 2) + 10


    print("MENU:")
    print()
    x = input("Deseja consultar o prazo de entrega? [S/N]:")
    if x == "S":
        a = input("Sua entrega é EntregaComum ou EntregaExpressa:")
        if a == "EntregaComum":
            dis1 = int(input("Distancia:"))
            pes1 = int(input("Peso:"))
            ent1 = EntregaComum(distancia=dis1, peso=pes1)
            print()
            print(f"Seu frete é de {ent1.calcular_frete()} reais.")

        elif a == "EntregaExpressa":
            dis2 = int(input("Distancia:"))
            pes2 = int(input("Peso:"))
            ent2 = EntregaExpressa(distancia=dis2, peso=pes2)
            print()
            print(f"Seu frete é de {ent2.calcular_frete()} reais.")
    else:
        print("Obrigado!")
        break
