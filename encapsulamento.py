class Conta:
    def __init__(self,nome, saldo):
        self._nome = nome
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if valor <= 0:
            raise ValueError("O valor da saldo deve ser positivo.")
            self._saldo = valor

c = Conta("Arthur", 100)

c.saldo = 1000
print(c.saldo)