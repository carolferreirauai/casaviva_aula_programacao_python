# Exercício 5:

# Desenvolva um programa que peça ao usuário para digitar 5 números
# inteiros. Ao final da leitura, o programa deve mostrar quantos desses
# números são maiores que 10.

# entrada de dados

contador = 0

for i in range (5):
    numero = int(input("Digite 5 números: "))

    # verificar os números maior que 10
    if numero > 10:
        contador += 1

# saída de dados
print("Quantidade de números maiores que 10: ", contador)