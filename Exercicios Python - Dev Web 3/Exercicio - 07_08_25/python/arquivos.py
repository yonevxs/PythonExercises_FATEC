#Criando arquivo de texto em python:

with open('aula.txt', 'w') as arquivo:
    arquivo.write('linha 01')

#w - escreve o conteúdo e sobrescreve

#a - adiciona ao final

with open('aula.txt', 'r') as arquivo:
    print(arquivo.read())

#Outra forma de ler o arquivo)
with open('aula.txt', 'r') as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(' ')
        print(lista)

#Pega cada linha e lê, capturando as linhas e tornando elas uma lista
#split - separa o conteúdo da linha por caractere específico 



# r - lê o arquivo