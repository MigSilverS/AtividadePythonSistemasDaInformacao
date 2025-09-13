# 40. Frutas e cores
frutas = {"maçã": "vermelha", "banana": "amarela", "uva": "roxa", "laranja": "laranja", "kiwi": "verde"}
# adicionando uma nova fruta
frutas["abacaxi"] = "amarelo"
for fruta, cor in frutas.items():
    print(fruta, "->", cor)