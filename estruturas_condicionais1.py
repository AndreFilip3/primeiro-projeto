nota = float(input("Digite a nota do aluno: "))

if nota >= 9:
    print("Excelente!\nAprovado! :)")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação!\nMelhore!")
else:
    print("REPROVADO!")
