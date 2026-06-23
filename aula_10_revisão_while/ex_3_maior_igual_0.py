# Exercícios 3:

# Crie um programa que leia números digitados pelo usuário. O
# programa deve continuar lendo enquanto o número digitado for maior
# ou igual a 0.

# Quando for digitado um número negativo, o programa deve parar e
# mostrar quantos números foram digitados.

numero = int(input())
quantidade = 0

while (numero >= 0):
    quantidade += 1
    numero = int(input())

print(quantidade)