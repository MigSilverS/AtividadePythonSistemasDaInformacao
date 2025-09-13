# 49. Dicionário aninhado de países
paises = {
    "Brasil": {"capital": "Brasília", "população": 210000000},
    "Argentina": {"capital": "Buenos Aires", "população": 45000000},
    "Chile": {"capital": "Santiago", "população": 19000000}
}
for pais, info in paises.items():
    print(f"A capital de {pais} é {info['capital']}")