class Aluno:
    def __init__(self, nome, nota):
        self._nome = nome
        self._aprovado = False
        self._nota = nota


    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10")
        self._nota = nota

        if nota >= 6:
            self._aprovado =  True
        else:
            self._aprovado = False

    @property
    def aprovado(self):
        return self._aprovado

n1 = Aluno("Arthur", 8)
print(n1.nota, n1._aprovado)

