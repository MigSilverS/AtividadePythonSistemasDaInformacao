numeros = [1,2,3,2,4,5,1,6,7,8,5,9,10,7,6]
lista_unica = []

for n in numeros:
    if n not in lista_unica:
        lista_unica.append(n)

print(lista_unica)
