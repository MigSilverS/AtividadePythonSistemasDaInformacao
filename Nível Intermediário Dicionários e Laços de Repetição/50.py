# 50. Pessoas e hobbies
hobbies = {
    "Ana": ["leitura", "música"],
    "Carlos": ["futebol", "viagem"],
    "Maria": ["leitura", "cinema"],
    "João": ["corrida", "natação"],
    "Fernanda": ["arte", "leitura"]
}
for nome, lista in hobbies.items():
    if "leitura" in lista:
        print(nome, "gosta de leitura")