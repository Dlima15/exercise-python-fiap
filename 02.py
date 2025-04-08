# Uma universidade realizará uma competição acadêmica. Para esta competição,
# só serão aceitos estudantes que sejam maiores de idade.
# Crie um programa que receba o RM e a idade de um aluno e exiba uma mensagem
# confirmando o estudante ser maior. Caso um aluno seja menor, informe ter
# autorização dos pais. O cadastro deve ser realizado e o email deve ser
# enviado para os responsáveis.
# Caso contrário, o cadastro não será feito.

rm = input("Qual a seu Rm?")
idade = int(input("Qual sua idade?"))

if idade >= 18:
    print(f"Seu cadastro foi realizado aluno {rm}")
    print("Prosseguiremos via email")
else:
    print("ERRO! Você tem autorização?")
    A = input("Seus pais autorizaram, S - sim ou N - não?")
    if A == "S":
        print("OK, prosseguiremos por email")
    else:
        print("infelizmente não será possivel continuar, tente a autorização ou espere ficar maior de idade!")


print("...")
print("...")


print("O Programa foi finalizado")
