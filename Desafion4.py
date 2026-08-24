class Ingresso:
    def __init__(self, evento, preco):
        self.evento = evento
        self.preco = preco

    def calcular_preco(self):
        return self.preco

    def __str__(self):
        return f"Evento: {self.evento} | Preço: R$ {self.calcular_preco():.2f}"

    def __repr__(self):
        return f"Ingresso(evento='{self.evento}', preco={self.preco})"


class IngressoInteiro(Ingresso):
    pass


class MeiaEntrada(Ingresso):
    def calcular_preco(self):
        return self.preco / 2


def ler_preco():
    while True:
        try:
            return float(input("Preço do ingresso (inteiro): R$ "))
        except ValueError:
            print("Valor inválido. Digite um número, ex: 100.00")


ingressos = []

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar Ingresso Inteiro")
    print("2. Cadastrar Meia-Entrada")
    print("3. Listar Ingressos")
    print("4. Ver Representação (__repr__)")
    print("5. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        evento = input("Nome do evento: ")
        preco = ler_preco()
        ingressos.append(IngressoInteiro(evento, preco))
        print(f"Ingresso inteiro cadastrado (R$ {preco:.2f})!")

    elif opcao == "2":
        evento = input("Nome do evento: ")
        preco = ler_preco()
        ingressos.append(MeiaEntrada(evento, preco))
        print(f"Meia-entrada cadastrada (R$ {preco / 2:.2f})!")

    elif opcao == "3":
        if not ingressos:
            print("Nenhum ingresso cadastrado.")
        else:
            for ing in ingressos:
                print(ing)

    elif opcao == "4":
        if not ingressos:
            print("Nenhum ingresso cadastrado.")
        else:
            for ing in ingressos:
                print(repr(ing))

    elif opcao == "5":
        print("Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.")