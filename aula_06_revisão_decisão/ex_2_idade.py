# Exercício 2

# Peça a idade do usuário. Se a idade for menor que 12, mostre "Criança".
# Se for entre 12 e 17, mostre "Adolescente". Se for 18 ou mais, mostre
# "Adulto".

# entrada de dados
idade = int(input("Digite a idade: "))

# classificar
# saída de dados
if idade < 12:
    print("Criança")
elif idade < 17:
    print("Adolescente")
elif idade >= 18:
    print ("Adulto")