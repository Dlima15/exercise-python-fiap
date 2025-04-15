# 2 – A compra de um veículo pode ser realizada parcelada. Crie um programa 
# que receba o valor de um carro e mostre uma tabela com os seguintes dados: 
# preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
#a) O preço final para compra à vista tem um desconto de 20%.
#b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.



# Simulação de pagamento de carro com desconto à vista ou parcelado com acréscimos

preco = float(input("Digite o preço do carro: "))

# À vista tem 20% de desconto
avista = preco * 0.8
print(f"\nO preço final à vista com desconto 20% é: R${avista:.2f}")

parcelas_opcoes = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

# Acréscimos a cada opção de parcelamento (mesma ordem da lista de parcelas)
acrescimos = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print()

for i in range(len(parcelas_opcoes)):
    qtd = parcelas_opcoes[i]
    taxa = acrescimos[i] / 100
    total = preco * (1 + taxa)
    parcela = total / qtd
    print(f"O preço final parcelado em {qtd}X é de R${total:.2f} com parcelas de R${parcela:.2f}")
