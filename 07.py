# Início do programa: Exibe título
print("Verificador de frequência cardíaca")

# Entrada da idade do usuário (conversão para inteiro)
idade = int(input("Qual a sua idade: "))

# Entrada da frequência cardíaca atual (BPM - batimentos por minuto)
bpm = int(input("Qual seu BPM atual? "))

# Verifica se a idade está na faixa de 0 a 2 anos
if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequência cardíaca adequada")
    else:
        print("Frequência cardíaca inadequada")

# Verifica se a idade está entre 8 e 17 anos
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequência cardíaca adequada")
    else:
        print("Frequência cardíaca inadequada")

# Verifica se a idade está entre 18 e 60 anos
elif idade >= 18 and idade <= 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequência cardíaca adequada")
    else:
        print("Frequência cardíaca inadequada")

# Verifica se a idade é maior que 60 anos
elif idade > 60:
    if bpm >= 50 and bpm <= 60:
        print("Frequência cardíaca adequada")
    else:
        print("Frequência cardíaca inadequada")

# Caso nenhuma faixa etária seja atendida
else:
    print("Não existem dados para a idade indicada")
