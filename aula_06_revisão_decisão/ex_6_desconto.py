# Exercício 6:

# Solicite ao usuário o valor total de uma compra. De acordo com esse
# valor, determine o desconto aplicado:

# Compras abaixo de 100 não recebem desconto;
# Compras entre 100 e 299 recebem 10% de desconto;
# Compras a partir de 300 recebem 20% de desconto;

# Ao final, exiba o valor que deverá ser pago.

# entrada de dados
valor = float(input("Qual o valor total da compra: "))

# desconto
# saída de dados
if valor < 100:
    print(valor)
elif valor < 299:
    print(valor - (valor * 0.1))
else:
    print(valor - (valor * 0.2))