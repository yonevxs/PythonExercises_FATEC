import csv
from filme import Filme
from cliente import Cliente

class Locadora:
    def __init__(self):
        self.filmes = []
        self.clientes = []

    def cadastrar_filme(self, filme):
        if isinstance(filme, Filme):
            self.filmes.append(filme)
            print(f'Filme: {filme.titulo} adicionado!')

            with open('filmes.csv', 'w', encoding='utf-8') as catalogoFilmes:
                catalogoFilmes.write('Codigo | Titulo | Genero | Ano | Disponivel\n')
                for filme in self.filmes:
                    linha = f'{filme.codigo}, {filme.titulo}, {filme.genero}, {filme.ano}, {filme.disponivel}\n'
                    catalogoFilmes.write(linha)
        else:
            print("Não é possível cadastrar esse filme!")

    def listar_filmes(self):
        print('Filmes da locadora')
        for filme in self.filmes:
            print(filme)

    def buscar_filme(self, titulo):
        for filme in self.filmes:
            if filme.titulo.lower() == titulo.lower():
                return filme
            else:
                return 'Filme não encontrado'

    def alugar_filme(self, filme, cliente):
        if isinstance(filme, Filme) and isinstance(cliente, Cliente):
            if filme.disponivel:
                filme.disponivel = False
                cliente.filmes_alugados.append(filme)
                print(f'Filme: {filme.titulo} alugado com por {cliente.nome}!')
            else:
                print(f'Filme: {filme.titulo} não está disponível para alugar')

    def devolver_filme(self, filme, cliente):
        if isinstance(filme, Filme) and isinstance(cliente, Cliente):
            if not filme.disponivel:
                filme.disponivel == True
                cliente.filmes_alugados.remove(filme)
                print(f'Filme: {filme.titulo} devolvido por {cliente.nome}')
            else:
                print(f'Filme: {filme.titulo} já está disponível')
    '''
    MÉTODOS DE CLIENTES
    '''
    def cadastrar_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.clientes.append(cliente)
            print(f'Cliente: {cliente.nome} adicionado!')

            with open('clientes.csv', 'w', encoding='utf-8') as catalogoClientes:
                catalogoClientes.write('Nome | CPF\n')
                for cliente in self.clientes:
                    linha = f'{cliente.nome}, {cliente.cpf}'
                    catalogoClientes.write(linha)
        else:
            print('Não é possível encontrar o cliente')

    def listar_clientes(self):
        print("Lista de Clientes")
        for cliente in self.clientes:
            print(cliente)
    

    def buscar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome.lower():
                return cliente
            else:
                return 'Cliente não encontrado'

