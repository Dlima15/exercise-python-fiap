#3 – Na oferta de um produto de crédito aos clientes, três informações são muito 
# #importantes apresentar ao cliente: valor da dívida, a taxa de juros e o número 
# de parcelas para pagamento do empréstimo contraído junto à Fintech. Faça um programa 
# que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:

 

# Entrada do valor da dívida
valor_divida = float(input("Digite o valor da dívida: "))

# Tabela: (quantidade de parcelas, % de juros)
opcoes = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]

# Exibe as opções
for parcelas, juros_percentual in opcoes:
    juros_valor = valor_divida * (juros_percentual / 100)
    total_com_juros = valor_divida + juros_valor
    valor_parcela = total_com_juros / parcelas
    print(f"Total: R$ {total_com_juros:.2f} Juros: R$ {juros_valor:.2f} Número de parcelas: {parcelas} Valor da Parcela: R$ {valor_parcela:.2f}")
