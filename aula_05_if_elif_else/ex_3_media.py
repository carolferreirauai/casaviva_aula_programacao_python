# Exercício 3:

# Desenvolva um código que receba duas notas de um aluno (de 0 a 10)
# e calcule a média. Se a média for maior ou igual a 6, exiba "Aprovado"
# na saída; caso contrário, exiba "Reprovado".

# entrada de dados
nota1 = int(input("Digita a nota 1: "))
nota2 = int(input("Digita a nota 2: "))

# calcule a média
media = (nota1 + nota2) / 2

# verifique se foi aprovado ou reprovado
# saida de dados
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")