# 34. Dicionário produtos e preços
produtos = {"arroz": 20, "feijão": 10, "macarrão": 5, "carne": 50, "leite": 6}
total = 0
for preco in produtos.values():
    total += preco
print("Valor total da compra:", total)
