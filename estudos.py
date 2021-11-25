import random 
lista = ["TESTE1", "TESTE2", "TESTE3", "TESTE4"]

# while True:
#     nome = input("Digite um nome de participante: ")
#     lista.append(nome)
#     resposta = input("Quer continuar? [S/N]").upper()
#     if resposta in "Nn":
#         break

lista.sort()

conjunto = dict()

while len(lista) > 0:
    print(lista)
    elemento = lista[0]
 #   lista.remove(elemento)
    par_elemento = random.choice(lista)
    conjunto[elemento] = par_elemento
 #   lista.remove(par_elemento)

print(conjunto)
