# Exibe título da votação
print("🎮 Votação de Console - Equipe de 5 Colaboradores 🎮")
print("Opções: PLAYSTATION, XBOX, NINTENDO\n")

# Inicializa os contadores de votos para cada console
votos_playstation = 0
votos_xbox = 0
votos_nintendo = 0

# Loop para receber os votos dos 5 membros da equipe
for i in range(1, 6):
    voto = input(f"Colaborador {i}, digite seu voto (PLAYSTATION, XBOX ou NINTENDO): ").strip().upper()
    
    if voto == "PLAYSTATION":
        votos_playstation += 1
    elif voto == "XBOX":
        votos_xbox += 1
    elif voto == "NINTENDO":
        votos_nintendo += 1
    else:
        print("Voto inválido! Não será contabilizado.")

# Verifica qual console recebeu mais votos
if votos_playstation > votos_xbox and votos_playstation > votos_nintendo:
    escolhido = "PLAYSTATION"
    votos = votos_playstation
elif votos_xbox > votos_playstation and votos_xbox > votos_nintendo:
    escolhido = "XBOX"
    votos = votos_xbox
elif votos_nintendo > votos_playstation and votos_nintendo > votos_xbox:
    escolhido = "NINTENDO"
    votos = votos_nintendo
else:
    escolhido = "Empate entre consoles"
    votos = "N/D"

# Exibe o resultado
print("\n🗳️ Resultado Final:")
print(f"Console escolhido: {escolhido}")
if votos != "N/D":
    print(f"Quantidade de votos: {votos}")
else:
    print("Houve empate. Será necessária nova votação.")
