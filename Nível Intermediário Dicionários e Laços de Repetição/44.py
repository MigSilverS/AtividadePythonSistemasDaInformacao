# 44. Lista de dicionários (livros)
livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo"}
]
for livro in livros:
    if livro["autor"] == "Machado de Assis":
        print(livro["titulo"])