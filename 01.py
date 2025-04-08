#Uma universidade realizará uma competição acadêmica. Para esta competição, só serão Aceitos estudantes que sejam maiores de idade
#crie um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso o estudante seja maior de idade, e uma mensagem de errp caso o estudande seja menor de idade

rm = input("Qual a seu Rm?")
idade = int(input("Qual sua idade"))

if idade >= 18:
    print(f"Seu cadastro foi realizado aluno {rm}")
    print("Prosseguiremos via email")
else:
    print("ERRO! Você é menor de idade tente novamente qauando tiver 18")

print("O programa foi Finalizado")    