# Exercício 4:

# Solicite ao usuário que informe a letra correpondente ao sue periodo
# de estudo.

# Ao digitar M, o programa deve indicar manhã.
# Ao digitar T, deve indicar Tarde.
# Ao digitar N, deve indicar Noite.

# Para qualquer outra opção, informe que o período é inválido.

# entrada de dados
periodo = input("Digite um período: ")

# classifique
# saída de dados
if periodo == "M":
    print("Manhã")
elif periodo == "T":
    print("Tarde")
elif periodo == "N":
    print("Noite")
else:
    print("Período Inválido!")