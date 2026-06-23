# Exercício 3:

# Escreva um programa que leia números inteiros que o usuário insere e
# calcule a soma de todos esses números. O laço deve continuar até que
# o usuário digite 0.

# Dica: Comece definindo uma variável soma com o valor inicial de 0
# (soma = 0). Esta variável será usada para acumular a soma dos
# números inseridos pelo usuário.

numero = int(input())
soma = 0

while numero != 0:
    soma += numero
    numero = int(input())

print (soma)