aluno = {
    'matricula' : '202502',
    'nome' : 'Mário',
    'curso' : 'DSM',
    'ciclo' : '3'
}

print(aluno)

#Exibe chave:valor
print(aluno.items())

#Exibe somente chaves
print(aluno.keys())

#Exibe somente valores
print(aluno.values())

#Adicionando item ao dicionario
aluno['periodo'] = 'vespertino'
print(aluno)

#Caso a chave já exista no dicionário, ele sobrepõe
aluno['ciclo'] = '5'
aluno.update({'ciclo':'6'})

#Removendo item
del aluno['periodo']

# Percorrendo os itens do dicionario por chave e valor
for chave, valor in aluno.items():
    print(chave, ": ", valor)

#Encontrando chave em if
if 'curso' in aluno:
    print("Encontrado")

print(aluno)
