# uma empresa de telefonia está realizando uma promoção, onde os clientes podem receber bônus para navegação na internet com base em uma pontuação
# 1000 pontos -> 3Gb de Bõnus 
# 500 pontos -> 1,5 Gb de Bônus 
# 200 pontos -> 500mb de Bônus 
# crie um programa que receba o número de pontos e informe ao cliente quantos bônus ele receberá 

P = int(input("Quantos pontos você tem ?"))

if P >= 1000:
    print("Vc recebeu 3Gb de Bônus")
elif P >= 500:
    print("Vc recebeu 1,5gb de Bônus")
elif P >= 200:
    print("Vc recebeu 500 mb de Bônus")
else:
    print("Vc nao ganhou bonus desta vez")