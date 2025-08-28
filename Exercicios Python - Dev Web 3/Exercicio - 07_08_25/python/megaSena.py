import random
 
#lista_sorteados = random.sample(range(1, 60), 6)
#print(lista_sorteados)

# Teste para uma lista já definida, apenas descomente a linha 3 para poder gerar uma lista aleatória!!!
lista_sorteados = [1, 4, 3, 5, 60, 43]
lista = []
print("Digite '0' para sair")
while len(lista) <= 20:
    num_lista = int(input("Digite seus numeros da sorte: "))
    if num_lista == 0:
        break
    if num_lista > 60:
        print("[ERRO] - Valor digitado é maior que 60!")
        break
    lista.append(num_lista)
print("Numeros sorteados: ", lista_sorteados)
print("Numeros escolhidos: ", lista)
print("-------------------")
print("Comparação")

comparacao = set(lista) & set(lista_sorteados)
acertos = len(comparacao)

if acertos >= 1:
    print(f"{acertos} acerto(s) - {comparacao}")
    print("Tente novamente!")
    if acertos == 4:
        print(f"4 acertos - {comparacao}")
        print("Você acertou uma QUADRA! Muito bom!")
    elif acertos == 5:
        print(f"5 acertos - {comparacao}")
        print("Você acertou uma QUINA! Muito bom!")
    elif acertos == 6:
        print(f"6 acertos - {comparacao}")
        print("Você acertou uma SENA! Parabéns, você ganhou!")
else:
    print("Poxa, nenhum acerto! Tente novamente.")


