# Exercício 5:

# Solicite ao usuário que digite uma nota. O programa deve continuar
# pedindo notas enquanto o valor informado for maior ou igual a 0.

# Quando o usuário digitar uma nota negativa, o programa deve parar e
# calcular a média apenas das notas válidas digitadas, exibindo o
# resultado na tela.

nota = float(input("Digite a nota: "))
soma = 0
quantidade = 0

while (nota >= 0):
    nota = float(input("Digite a nota: "))
    if nota >= 0:
        soma += nota
        quantidade += 1

media = soma / quantidade
print(media)