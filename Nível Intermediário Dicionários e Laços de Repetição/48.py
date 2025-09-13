# 48. Produto disponível ou não
produto = {"nome": "Notebook", "preço": 3500, "disponível": True}
for chave, valor in produto.items():
    if chave == "disponível":
        if valor:
            print(f"O produto {produto['nome']} está disponível")
        else:
            print(f"O produto {produto['nome']} está indisponível")