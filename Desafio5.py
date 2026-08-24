class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def inscricao(self):
        return f"A matrícula de {self.nome} é {self.matricula} e seu curso é {self.curso}."

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina

    def trabalho(self):
        return f"O salário de {self.nome} é de R${self.salario:} e sua disciplina é {self.disciplina}."


aluno1 = Aluno("Arthur", 19, "G09NA21L", "CDD")
professor1 = Professor("Octávio", 34, 50000, "Programação")

print(aluno1.inscricao())
print(professor1.trabalho())
