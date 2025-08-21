nome = input("Digite o nome do astronauta: ")
sup_dicionario = {
    "1" : ["Água", 200],
    "2" : ["Comida", 350],
    "3" : ["Roupas", 150],
    "4" : ["Oxigenio", 350],
    "5" : ["Combustivel", 400]
} 
soma = 0

while soma < 1000:
    print(sup_dicionario)
    opcao = input("\nEscolha os suprimento: ")

    if opcao.lower() == 'fim':
        break

    opcoes = [opcao]
    soma += sup_dicionario[opcao][1]
    print("Capacidade máxima: 1000kg - Capacidade atual: ",soma)

    if soma > 1000:
        print("\nEXCEDEU O LIMITE DE PESO - 1000kg")
        print("Peso:", soma)
        soma = 0
        break


print("\nAstronauta:", nome)
print("Carga utilizda:", soma)
print("Carga restante:", (1000 - soma))