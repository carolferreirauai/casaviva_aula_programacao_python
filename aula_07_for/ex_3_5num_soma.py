# Exercício 3

# O programa deve ler exatamente 5 números inteiros digitados pelo
# usuário. Após a leitura de todos os valores, o programa deve calcular e
# mostrar a soma desses números.

# declaração de variáveis
soma = 0

for i in range (0, 5):
    # entrada de dados
    numero = int(input("Digite 5 números: "))
    
    # calculo da soma
    soma += numero

# saida de dados
print("A soma dos número é: ", soma)