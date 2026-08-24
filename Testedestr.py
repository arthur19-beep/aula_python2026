class Aluno:
    def __init__(self, nome, nota):
        self._nome = nome
        self._aprovado = False
        self.nota = nota  # Usa o setter para garantir a validação e o cálculo inicial

    @property
    def nome(self):
        return self._nome

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10")
        self._nota = nota

        if nota >= 6:
            self._aprovado = True
        else:
            self._aprovado = False

    @property
    def aprovado(self):
        return self._aprovado

    def __repr__(self):
        return f"Aluno(nome='{self._nome}', nota={self._nota})"

    def __str__(self):
        status = "Aprovado" if self._aprovado else "Reprovado"
        return f"Aluno: {self._nome} | Nota: {self._nota} | Status: {status}"


aluno1 = Aluno("Arthur", 9.5)
print(aluno1)

print(repr(aluno1))