# Dividindo o código em pequenas funções para organizar melhor

def pedir_nome():
    return input("Digite seu nome: ")

def exibir_mensagem(nome):
    print(f"Olá, {nome}, bom estudo!")

# Programa principal
nome_usuario = pedir_nome()
exibir_mensagem(nome_usuario)
