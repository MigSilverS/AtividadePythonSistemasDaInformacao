# 28. Ordem decrescente
numeros = [1, 5, 9, 3, 7, 2, 8, 4, 6, 10]
ordenados = []
for n in sorted(numeros, reverse=True):
    ordenados.append(n)
print("Decrescente:", ordenados)