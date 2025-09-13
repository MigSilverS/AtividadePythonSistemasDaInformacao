# 45. Estoque de produtos
estoque = {"arroz": 5, "feijão": 12, "macarrão": 8, "carne": 20, "leite": 3}
for produto, qtd in estoque.items():
    if qtd < 10:
        print(produto, "- Estoque baixo!")