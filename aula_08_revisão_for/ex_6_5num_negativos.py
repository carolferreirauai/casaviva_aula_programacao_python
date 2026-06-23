# Exercício 8:

# Desenvolva um programa que peça ao usuário digitar 5 números e 
# avise quando um número for negativo

for i in range (5):

    # entrada de dados
    numero = int(input("Digite 5 números: "))

    if (numero < 0):
        print ("Número negativo!")