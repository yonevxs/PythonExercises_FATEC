class Filme:
    def __init__(self, titulo, genero, ano, codigo, disponivel):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.codigo = codigo
        self.disponivel = True

    def __str__(self):
        status = 'Sim' if self.disponivel else 'Não'
        return f'{self.codigo} | {self.titulo} | {self.genero} | {self.ano} | {status}'