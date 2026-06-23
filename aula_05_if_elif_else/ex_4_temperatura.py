# Exercícios 4:
# Desenvolva um código que receba uma temperatura e classifique o
# valor informado da seguinte forma:

# Se for menor que 10, exiba "Frio";
# Se for maior ou igual a 10 e menor que 25, exiba "Agradável";
# Se for maior ou igual a 25 e menor que 35, eciba "Quente";
# Caso contrário, exiba "Muito quente".

# entrada de dados
temperatura = int(input("Digita a temperatura: "))

# classificar
# saida de dados
if temperatura < 10:
    print("Frio")
elif temperatura < 25:
    print("Agradável")
elif temperatura < 35:
    print("Quente")
else:
    print("Muito quente")