#1 – A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a 
# controlar suas fontes de receitas, gastos, dívidas e investimentos.  Ela precisa 
# realizar uma votação para escolher qual dia da semana é o melhor para a realização 
# das lives com o time da mentoria financeira. Desenvolva um programa em que os colaboradores 
# informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) 
# da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.

# Votação para escolher o melhor dia da semana para a live

votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

num_colaboradores = int(input("Informe o número de colaboradores: "))

for i in range(num_colaboradores):
    voto = input("Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").strip().lower()
    if voto in votos:
        votos[voto] += 1
    else:
        print("Dia inválido! Esse voto não vai contar 😬")

# Bora descobrir qual dia venceu
max_votos = max(votos.values())
dias_mais_votados = [dia for dia, qtd in votos.items() if qtd == max_votos]

print("\n🗳️ Resultado da votação:")
if len(dias_mais_votados) == 1:
    print(f"O dia escolhido pelos colaboradores é: {dias_mais_votados[0]}")
else:
    print(f"Empatou! Dias mais votados: {', '.join(dias_mais_votados)} com {max_votos} votos cada.")
