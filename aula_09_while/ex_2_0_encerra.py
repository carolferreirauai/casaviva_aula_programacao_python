# Exercício 2:

# Escreva um programa que peça um número ao usuário e continue
# pedindo até que ele digite o número 0. Quando o 0 for digitado, o
# programa deve encerrar.

numero = int(input("Digite um número: "))

while numero != 0:
    numero = int(input("Digite um número: "))
    
print ("Programa Encerrado!")