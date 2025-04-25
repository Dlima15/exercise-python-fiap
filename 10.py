#Repetições e condições

resposta = ""
tentativas = 0

while resposta != "42":
    resposta = input("Qual é a reposta da vida, do universo e tudo mais? ")
    tentativas = tentativas + 1

print("Parabéns vc acertou xxxxxxxx n não esqueça seu tenis")

print(f"Você teve {tentativas} chances")