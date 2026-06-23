# Exercício 5

# Peça ao usuário que informe seu peso (em kg) e sua altura (em metros).
# Calcule o IMC usando a fórmula:

# IMC = peso / (altura * altura)

# Após po cálculo, mostre a classificação:

# Abaixo de 18.5, "Abaixo do peso";
# Entre 18.5 e 24.9, "Peso normal";
# Entre 25 e 29.9, "Sobrepeso"
# 30 ou mais, "Obesidade".

# entrada de dados
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# calcule o imc
imc = peso / (altura * altura)

# saida de dados
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")