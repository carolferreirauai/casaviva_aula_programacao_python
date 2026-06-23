# Exercício 5:

# Crie um programa que receba o salário atual de um funcionário e o seu
# tempo de trabalho em anos. O programa deve verificar o tempo o de
# trabalho informado e aplicar um reajuste salarial conforme as regras:

# Funcionários com menos de 1 ano não recebem reajuste;
# De 1 a 3 anos recebem 5%;
# De 4 a 6 anos recebem 10%;
# Acima de 6 anos recebem 15%;

# Ao final, o programa deve calcular e exibir o novo salário.

# entrada do dados
salario = int(input("Digite o salário: "))
tempo = int(input("Digite o tempos em anos: "))

# verificar o tempo
# aplicar o reajuste
# saida de dados
if tempo < 1:
    print(salario)
elif tempo <= 3:
    print(salario * 1.05)
elif tempo <= 6:
    print(salario * 1.10)
else:
    print (salario * 1.15)