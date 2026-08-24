from abc import ABC, abstractmethod

class Mensagem(ABC):
    def __init__(self, texto):
        self.texto = texto

    @abstractmethod
    def enviar_mensagem(self):
        pass

class Email(Mensagem):
    def __init__(self, texto, destinatario):
        super().__init__(texto)
        self.destinatario = destinatario

    def enviar_mensagem(self):
        return f"Mensagem enviada para {self.destinatario} | Conteúdo: {self.texto}"

class SMS(Mensagem):
    def __init__(self, texto, nuemro):
        super().__init__(texto)
        self.nuemro = nuemro

    def enviar_mensagem(self):
        return f"Mensagem enviada para {self.nuemro} | Conteúdo: {self.texto}"

while True:
    a = input("Menu\n"
              "1 - Enviar E-mail;\n"
              "2 - Enviar SMS;\n"
              "3 - Sair.\n"
              "Opção:")
    if a == "1":
        b = input("Digite o e-mail: ")
        c = input("Digite o texto: ")
        email1 = Email(c, b)
        print(email1.enviar_mensagem())

    elif a == "2":
        d = input("Digite o número: ")
        e = input("Digite o texto: ")
        zap1 = SMS(d, e)
        print(zap1.enviar_mensagem())

    elif a == "3":
        print("Saindo!")
        break



