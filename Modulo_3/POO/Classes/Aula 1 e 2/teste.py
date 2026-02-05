import random,time

# Lista de padrões
padroes = [
    "Factory Method",
    "Observer",
    "Singleton",
    "Strategy"
]

# Lista de equipes
equipes = [
    "Equipe 1",
    "Equipe 2",
    "Equipe 3",
    "Equipe 4"
]

# Embaralha a lista de padrões
random.shuffle(padroes)

# Sorteio dos pares
print("Resultado do sorteio:\n")
for equipe, padrao in zip(equipes, padroes):
    print(f"{equipe} -> {padrao}")
    #pausa um segundo antes de imprimir o próximo sorteio
    time.sleep(1)
