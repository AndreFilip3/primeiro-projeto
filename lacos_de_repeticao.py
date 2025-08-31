'''for i in range(10):
    print("Repetição número", i)'''

''' contador = 0
while contador < 5:
    print("Número:", contador)
    contador += 1 '''


'''senha = int(input("Digite uma senha numérica: "))

while senha != 1234:
    senha = int(input("Senha incorreta. Tente novamente\nDigite uma senha numérica: "))

    print("Você acertou a senha!\nAcesso permitido!")'''

while True:
    try:
        senha = int(input("Digite a senha: "))
        if senha == 1234:
            (print("Acesso permitido!"))
            break #encerra o loop
        else:
            print("Senha incorreta. Tente novamente!")
    except ValueError:
        print("Digite apenas números!")