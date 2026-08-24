#Arthur Barth,Dante Loss, Nathan Mendes e Piettro Capuccino.

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






guerreiro = Personagem("Guerreiro", 9, 3, 5)


mago = Personagem("Mago", 8, 4, 7)


mago.ataque2(guerreiro)
