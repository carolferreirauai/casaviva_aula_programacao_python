# Exercício 1:

# Peça ao usuário que digite uma senha. Se a senha for igual a
# "cas@viva", mostre na saída "Acesso concedido!". Caso contrário,
# mostre "Senha incorreta!".

# entrada de dado
senha = input("Digite a senha: ")

# verificar o acesso
if senha == "cas@viva":
    print("Acesso concedido!")
else:
    print("Senha incorreta!")