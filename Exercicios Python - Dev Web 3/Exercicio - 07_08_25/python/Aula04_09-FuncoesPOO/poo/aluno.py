#nome do arquivo, método que deseja
from pessoa import Pessoa

# Herdando classe Pessoa
class Aluno(Pessoa):
    def __init__(self, id, nome, curso, periodo):
        super().__init__(id, nome) # Herdando o construtor(init) da classe pai(Pessoa)
        self.curso = curso
        self.periodo = periodo

    # Sobreescrita de métodos
    def exibir(self):
        print(f"ID: {self.id} - Nome: {self.nome} - Curso: {self.curso} - Período: {self.periodo}")
a = Aluno(500, 'Fulano', 'DSM', 'Vespertino')
print(a.nome)
a.exibir()