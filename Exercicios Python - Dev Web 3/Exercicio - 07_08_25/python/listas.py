print("AUla 02 - Python")

lista = ['Ana', 'Maria', 'Braga', 'Louro']

print(lista)
print(lista[2])

#Quantos elementos tem nessa lista - len()
print("Elementos: ", len(lista))

#insere elementos na lista na posição que você definir - insert(posicao, valor)
lista.insert(3, 'José')
print(lista)

# adiciona no final de um array - append()
lista.append('João')
print(lista)

lista1 = [5,2,50,8,120]
print(lista1)

#juntando listas
lista.extend(lista1)
print(lista)

letras = ['f', 'a', 'c', 'b', 'e']

#Ordem crescente
letras.sort()
print(letras)

#Ordem decrescente
letras.sort(reverse=True)
print(letras)

#Pegando o último item
print(letras[-1])

#Removendo elementos da lista - del
nomes = ['Ana', 'Paula', 'Silva', 'Santos']
del nomes[2]
print(nomes)

#Remove elemento específico - remove
nomes.remove('Santos')
print(nomes)

#Remove pelo índice - pop(index)
nomes.pop(1)
print(nomes)
#del nomes - Exclui lista inteira

#Remove todos os elementos da lista
nomes.clear()
print(nomes)

nomes.append("Fábio")
print(nomes[0])