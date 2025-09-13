# 38. Cidades com mais de 1 milhão de habitantes
populacao = {
    "São Paulo": 12000000,
    "Rio de Janeiro": 6500000,
    "Campinas": 1200000,
    "Curitiba": 900000,
    "Santos": 433000
}
for cidade, habitantes in populacao.items():
    if habitantes > 1000000:
        print(cidade)