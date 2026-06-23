# Exercício 4:

# O programa deve pedir ao usuário que digite 3 números inteiros. Para
# cada número digitado, o programa deve informar se ele é impar ou não 
# é impar.

for i in range (3):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print ("Resultado: O número NÃO é IMPAR")
    else:
        print ("Resultado: O número é IMPAR")