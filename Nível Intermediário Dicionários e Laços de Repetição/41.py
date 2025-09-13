# 41. Lista com nomes de pessoas com mais de 30 anos
pessoas = {"Ana": 25, "Carlos": 35, "Maria": 28, "João": 40, "Fernanda": 32}
maiores_30 = []
for nome, idade in pessoas.items():
    if idade > 30:
        maiores_30.append(nome)
print("Com mais de 30 anos:", maiores_30)