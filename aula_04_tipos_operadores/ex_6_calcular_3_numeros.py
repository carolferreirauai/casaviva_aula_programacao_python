# Exercício 6:
# Desenvolva um programa que peça ao usuário três números e realize as
# seguintes operações: calcule a soam total, o produtos entre eles e
# verifique, usando operadores de comparação, se a soma é maior que o
# produto. Exiba todos os resultados na saída

# entrada de dados
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite outro número: "))

# faça a soma e o produto
soma_total = numero1 + numero2 + numero3
produto = numero1 * numero2 * numero3

# verifique se a soma é maior que o produto
maior = soma_total > produto

print("Soma total: ", soma_total)
print("Produto: ", produto)
print("Soma maior que produto: ", maior)
