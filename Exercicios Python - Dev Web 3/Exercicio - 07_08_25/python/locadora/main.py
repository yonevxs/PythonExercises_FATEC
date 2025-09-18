from filme import Filme
from locadora import Locadora
from cliente import Cliente

# filme1 = Filme("O Poderoso Chefão", 'Drama', 1972, 2530, True)
# locadora.cadastrar_filme(filme1)

# filme1.exibir()
locadora = Locadora()

while True:
    print("\n--- Menu ---")
    print("1. Cadastrar filme")
    print("2. Cadastrar cliente")
    print("3. Listar clientes")
    print("4. Listar filmes")
    print("5. Alugar filme")
    print("6. Devolver filme")
    print("7. Sair")

    opcao = input('Escolha sua opção: ')

    if opcao == '1':
        titulo = input('Título do filme: ')
        genero = input('Gênero: ') 
        ano = int(input('Ano de lançamento: ')) 
        codigo = int(input('Código: ')) 
        disponivel = input('Está disponivel: ')

        filme = Filme(titulo, genero, ano, codigo, disponivel)
        locadora.cadastrar_filme(filme)

    elif opcao == '2':
        nomec = input('Nome: ')
        cpf = int(input('CPF: '))

        cliente = Cliente(nomec, cpf)
        locadora.cadastrar_cliente(cliente)

    elif opcao == '3':
        locadora.listar_clientes()

    elif opcao == '4':
        locadora.listar_filmes()

    elif opcao == '5':
        print("Alugar Filme")
        nomef = input('Digite o nome do filme: ')
        filme_alugar = locadora.buscar_filme(nomef)

        clientef = input('Cliente que deseja alugar o filme: ')
        cliente_alugar = locadora.buscar_cliente(clientef)

        if filme_alugar and cliente_alugar:
            locadora.alugar_filme(filme_alugar, cliente_alugar)
        else:
            print("Filme ou cliente não encontrado")

    elif opcao == '6':
        print("Devolver Filme")
        nomef = input('Digite o nome do filme: ')
        filme_devolver = locadora.buscar_filme(nomef)

        clientef = input('Cliente que deseja devolver o filme: ')
        cliente_devolver = locadora.buscar_cliente(clientef)

        if filme_devolver and cliente_devolver:
            locadora.devolver_filme(filme_devolver, cliente_devolver)
        else:
            print('Filme ou cliente não encontrado')
    elif opcao == '7':
        break



