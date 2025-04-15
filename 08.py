# Solicita ao usuário o valor bruto da viagem
valor_bruto = float(input("Por favor, informe o valor bruto da viagem: "))

# Solicita ao usuário a categoria da viagem
categoria = input("Por favor, informe a categoria: Econômica, Executiva ou Primeira Classe: ")

# Solicita ao usuário a quantidade de viajantes
quantidade_viajantes = int(input("Por favor, informe a quantidade de viajantes: "))

# Inicializa o valor do desconto
valor_desconto = 0

# Verifica a categoria escolhida e calcula o desconto conforme a quantidade de viajantes
if categoria.upper() == "ECONÔMICA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.05

elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.08

elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.10
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.20

else:
    print("Categoria inexistente, tente novamente.")

# Calcula o valor líquido (com desconto)
valor_liquido = valor_bruto - valor_desconto

# Calcula o custo médio por passageiro
media_viajante = valor_liquido / quantidade_viajantes

# Exibe os resultados
print("O valor da viagem é de R${:.2f}. Após os descontos no valor de R${:.2f}, a viagem custará R${:.2f}. Cada passageiro tem um custo médio de R${:.2f}.".format(
    valor_bruto, valor_desconto, valor_liquido, media_viajante
))
