#Uma lanchonete trabalha com diversos combos de lanches, conforme a tabela abaixo:
#COMBO 1 = Hamburguer - R$12,50
#COMBO 2 = Cheeseburguer R$15,00
#COMBO 3 = X-bacon - R$17,50
#Crie um programa que receba o nummero de um combo e exiba o nome do lanche e preço correspondente 

numero_combo = int(input("Qual numero do combo desejado?"))

match numero_combo:
    case 1:
        nome_prato ="Hamburguer"
        valor =12,50
    case 2:
        nome_prato ="Cheeseburguer"
        valor =15,00
    case 3:
        nome_prato ="X-bacon"
        valor =17,50
    case _:
        nome_prato=None
        valor= None


if nome_prato:
    print(f"O combo desejado é o lanche{nome_prato} e custa o valor de R${valor}")

    
    
