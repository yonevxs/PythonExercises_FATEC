class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.filmes_alugados = []

    def __str__(self):
        return f'{self.nome} | {self.cpf}'