from random import choice
print("Feliz Natal")
lista = []
while True:
    nome = input("Digite o nome dos participantes: ")
    lista = [nome]
    resposta = input("Quer continuar? [S/N]").upper()
    if resposta in "Nn":
        break
sorteado = (f"{choice(lista)}\n")
print(f"O nome sorteado foi{sorteado}")
