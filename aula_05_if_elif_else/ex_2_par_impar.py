# Exercício 2
# Escreva um programa que leia um número inteiro e informe se ele é
# par ou ímpar.

# Dica: Um número é par se o resto da divisão (%) por 2 for igual a 0.
# Caso contrário, ele é impar.

# entrada de dados
numero = int(input("Digite um número: "))

# verificar se é par ou impar
# saída de dados
if numero % 2 == 0:
    print ("Par!")
else:
    print ("Impar!")