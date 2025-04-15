# 4 – Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema 
# deve calcular a alíquota de imposto de renda (IR) que deve ser aplicada sobre aquele 
# resgate, levando em consideração o número de dias que o valor permaneceu aplicado, de 
# acordo com a tabela abaixo:

#Até 180 dias = alíquota de 22,5% de IR.

#De 181 a 360 dias = alíquota de 20% de IR.

#De 361 a 720 dias = alíquota de 17,5% de IR.

#Acima de 720 dias = alíquota de 15% de IR.

 #____________________________________________________________________________________

# Exibe o menu de investimentos
print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

# Solicita o tipo de investimento
tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# Verifica se é um tipo válido
if tipo not in [1, 2, 3]:
    print("Tipo de investimento inválido.")
else:
    valor_resgate = float(input("Digite o valor a ser resgatado: "))
    dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

    if tipo == 1:  # CDB – tem imposto
        if dias <= 180:
            aliquota = 22.5
        elif dias <= 360:
            aliquota = 20.0
        elif dias <= 720:
            aliquota = 17.5
        else:
            aliquota = 15.0
        imposto = valor_resgate * (aliquota / 100)
        print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")
    else:  # LCI e LCA – isentos
        print("Este investimento é isento de imposto de renda.")