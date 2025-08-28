print("Vamos verificar se você pode dirigir!")

try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Por favor, digite apenas números!")
    
if idade >= 18:
    print("Pode dirigir!\nVocê é maior de idade!")
else:
    print("Não pode dirigir!\nVocê é menor de idade!")

