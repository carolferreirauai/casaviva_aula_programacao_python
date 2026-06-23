# Exercício 2:

# Escreva um programa que leia um número inteiro, calcule a tabuada
# desse número de 1 a 10 e, por fim, mostre os resultados na saída.

# entrada de dados
numero = int(input("Digite o número: "))

# tabuada de 0 a 10
# saida de dados
for i in range (1, 11):
    tabuada = numero * i
    print(tabuada)