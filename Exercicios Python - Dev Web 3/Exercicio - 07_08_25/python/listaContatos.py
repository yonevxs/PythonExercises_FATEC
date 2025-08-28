lista_contatos = {}
 
while True:
    print ('\nLista de Contatos')
    print('-------------------')
    print('1 - Cadastrar contato \n2 - Buscar contato \n3 - Excluir contato \n4 - Sair (Digite "exit" para sair)')
    opcao = input('\nEscolha seu modulo: ')
    print('----------------------')
    if opcao == 'exit':
        break
    if opcao == '1':
        nomectt = input('\nNome do Contato: ')
        if nomectt in lista_contatos:
            atualizar = input("Usuário já encontrado! Deseja atualizar o numero do contato?: ")
            if atualizar.lower() == 'sim':
                novo_numero = input("Digite o numero novo do contato: ")
                lista_contatos[nomectt] = novo_numero
                if nomectt in lista_contatos:
                    print(f"Numero atualizado! Nome: {nomectt}, Telefone: {lista_contatos[nomectt]}")
            else:
                print("Nenhum dado foi alterado")
        else:        
            telctt = input('Telefone: ')
            lista_contatos[nomectt] = telctt

    elif opcao == '2':
        nomectt = input('Nome do Contato a ser buscado: ')
        if nomectt in lista_contatos:
            print(f"Contato encontrado! Nome: {nomectt}, Telefone: {lista_contatos[nomectt]}")
        else:
            print('Contato não encontrado.')
    elif opcao == '3':
        excluir_ctt = input("Nome do contato que deseja excluir: ")
        if excluir_ctt in lista_contatos:
            print(f"Contato excluido com sucesso! Nome: {excluir_ctt}, Telefone: {lista_contatos[excluir_ctt]}")
            del lista_contatos[excluir_ctt]
        else:
            print(f"O contato {excluir_ctt} não existe na lista de contatos!")