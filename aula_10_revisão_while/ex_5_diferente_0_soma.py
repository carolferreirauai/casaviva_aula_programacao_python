# Exercício 5:

# Crie um programa que leia números digitados pelo usuário enquanto o
# valor digitado for diferente de 0.

# Quando o 0 for digitado, o programa deve parar e mostrar a soma de todos
# os números digitados.

numero = int(input())
soma = 0

while(numero != 0):
    soma += numero
    numero = int(input())

print (soma)