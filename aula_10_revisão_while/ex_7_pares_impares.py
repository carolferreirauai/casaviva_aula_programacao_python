# Exercício 7:

# Crie um programa que leia vários números inteiros. O programa deve
# parar quando o usuário digitar 0. Ao final, mostre quantos números
# pares e quantos números impares foram digitados.

numero = int(input())

while (numero != 0):
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    numero = int(input())

print("Pares: ", pares)
print("Ímpares: ", impares)