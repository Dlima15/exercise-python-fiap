#Durante o aniversário de sua fundação, uma loja está presenteando clientes da seguinte forma:
#Todas as compras no valor superior a R$1000, receberão um desconto de 10%.
#clientes selecionados receberam o cupom FESTA, que também gera 10% de desconto na hora da compra, não importando o valor 
#Os descontos Não são Cumulativos.


valor_compra =float(input("Qual valor da compra Realizada"))
Cupom = input("Tem um cupom ?")

if valor_compra >= 1000 or Cupom == "FESTA":
    valor_compra = valor_compra * 0.9
else:
    print("Compra sem desconto")

print(f"A sua compra teve o valor de R${valor_compra}")


