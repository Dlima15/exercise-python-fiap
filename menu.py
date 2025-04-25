op = 0

while op != 4:
    print("Menu de opções embarcações whatsapp")
    print("Selecione a embarcação que procura no mercado")
    print("1 - Embarcações de 18 a 26 pés")
    print("2 - Embarcações de 26 a 40 pés")
    print("3 - Embarcações de 40 a 80 pés")
    print("4 - Sair do sistema")

    op = int(input("Digite a sua opção: "))

    if op == 1:
        print("Um de nossos consultores especializados em 18 a 26 pés entrará em contato")
    elif op == 2:
       print("Um de nossos consultores especializados em 26 a 40 pés entrará em contato")
    elif op == 3: 
       print("Um de nossos consultores especializados em 40 a 80 pés entrará em contato")
    elif op == 4:
       print("Saindo do sistema")
    elif op != 1 and op != 2 and op != 3 and op != 4: 
       print("Opção invalida")