class Conta:
    def __init__(self, descricao, valor, vencimento, status):
        self.descricao = descricao
        self.valor = valor
        self.vencimento = vencimento
        self.status = status

    def pagar(self):
        self.status = "Pago"
        print(f"Conta de {self.descricao} no valor de: R${self.valor} foi paga!")

contas = []

while True:

    x = input("Deseja cadastrar alguma conta? [S/N]:")
    if x == "S":
        print("MENU")
        print()
        co = input("Conta: ")
        va = int(input("Valor: "))
        ve = input("Vencimento: ")
        st = input("Status: ")

        cadastro = Conta(co, va, ve ,st)
        contas.append(cadastro)
        print("Sua conta tem ID: ", len(contas)-1)

    elif x == "N":
        print("Deseja pagar alguma conta? [S/N]:")
        print()
        id = int(input("Digite o ID a ser pago: "))
        contas[id].pagar()
        print(f"Conta de {contas[id].descricao} no valor de: R$ {contas[id].valor} foi paga!")





    for i in range(len(contas)):
        print(f"Conta: {contas[i].descricao}| Valor: R${contas[i].valor}| Vencimento: {contas[i].vencimento}| Status: {contas[i].status}")


