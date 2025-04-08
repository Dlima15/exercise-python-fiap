rm = input("Qual a seu Rm?")
idade = int(input("Qual sua idade"))

if idade >= 18:
    print(f"Seu cadastro foi realizado aluno {rm}")
    print("Prosseguiremos via email")
else:
    print("Você é menor de idade tente novamente qauando tiver 18")

print("O programa foi Finalizado")    