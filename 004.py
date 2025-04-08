#sistema de Login

username = input("Qual seu usuario:") 
senha = input("Qual sua senha?")

if username.lower() == "Rick_morty" and senha == "15012005":
    print("login efetuado com sucesso!")
else:
    print("Senha incorreta!")