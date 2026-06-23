# Exercício 4:

# Escreva um programa que solicite uma senha ao usuário. Enquanto a 
# senha digitada for diferente de 1234, o programa deve continuar 
# pedindo a senha.

# Quando a senha correta for informada, o programa deve exibir a 
# mensagem "Acesso permitido".

senha = int(input("Digite a senha: "))

while (senha != 1234):
    senha = int(input("Digite a senha: "))

print("Acesso permitido")