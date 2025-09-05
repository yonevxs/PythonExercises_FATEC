#import json

livros = {}
ids = list(range(1, 101)) #Gerando IDs

while True:
    print("Sistema de Biblioteca")
    print("---------------------")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")

    opcao = input("Escolha sua opção: ")

    if opcao.lower() == 'exit':
        break

    if opcao == '1':
        print("Cadastrar Livro")
        nome_livro = input("Título: ")
        autor_livro = input("Autor: ")
        if ids:
            id_livro = ids.pop(0)
            livros[id_livro] = [nome_livro, autor_livro]

            print("Livro cadastrado!")
            print(f"ID: {id_livro} | Título: {nome_livro} | Autor: {autor_livro}")

            with open('livros.txt', 'w') as catalogoLivros:
                for id_livro, dados_livro in livros.items():
                    nome_livro, autor_livro = dados_livro
                    linha = f"{id_livro} | {nome_livro} | {autor_livro}\n"
                    catalogoLivros.write(linha)

                #with open('livros.json', 'w') as catalogoLivros:
                # #json.dump(livros, catalogoLivros)
        else:
            print("Não há IDs suficientes para cadastro!") 

    elif opcao == '2':
        print("Livros no Catálogo")
        with open('livros.txt', 'r') as catalogoLivros:
            for linha in catalogoLivros: 
                lista = linha.strip().split(' | ')
                print(lista)
    elif opcao == '3':
        print("Pesquisar")
        pesquisa = input("Autor ou Título: ").strip().lower()
        encontrado = []

        if livros:
            for id_livro, dados_livro in livros.items():
                nome_livro, autor_livro = dados_livro
                if pesquisa in nome_livro.lower() or pesquisa in autor_livro.lower():
                    encontrado.append((id_livro, nome_livro, autor_livro))
        if encontrado:
            print(f"\n{pesquisa} Encontrado(a)!")
            for livro in encontrado:
                id_livro, nome_livro, autor_livro = livro
                print(f"ID: {id_livro} | Título: {nome_livro} | Autor: {autor_livro}")
        else:
            print("Não foi possível encontrar esse livro ou autor!")


    