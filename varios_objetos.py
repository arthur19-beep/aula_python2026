class Personagem:
    def __init__(self, nome, energia, ataque, moeda):
        self.nome = nome
        self.energia = energia
        self.ataque = ataque
        self.moeda = moeda

    def ataque2(self, jogador):
        jogador.energia = jogador.energia-self.ataque
        if jogador.energia < 1:
            print(f"O {jogador.nome} morreu!")
        else:
            print(f"O {jogador.nome} recebeu {self.ataque} de dano e sua energia é de {jogador.energia}")



personagens = []

personagem = Personagem("P1", 10, 3, 5)
personagens.append(personagem)
print("Seu persoagem tem ID: ", len(personagens)-1)

personagem = Personagem("P2", 10, 3, 5)
personagens.append(personagem)
print("Seu persoagem tem ID: ", len(personagens)-1)


for i in range(len(personagens)):
    print(personagens[i].nome, personagens[i].energia, personagens[i].ataque, personagens[i].moeda)


