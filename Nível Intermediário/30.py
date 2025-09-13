# 30. Contar strings que começam com 'P'
palavras = ["Python", "PHP", "Perl", "Java", "Pascal", "Ruby"]
contador = 0
for p in palavras:
    if p.startswith("P"):
        contador += 1
print("Quantidade que começam com 'P':", contador)