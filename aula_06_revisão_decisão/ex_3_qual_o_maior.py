# Exercício 3

# Peça dois números ao usuário. Verifique qual deles é maior ou se os 
# dois são iguais e mostre o resultado.

# entrada de dados
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

# classifique
# saída de dados
if numero1 > numero2:
    print("O primeiro número é maior!")
elif numero2 > numero1:
    print("O segundo número é maior!")
else:
    print("Os dois números são iguais!")