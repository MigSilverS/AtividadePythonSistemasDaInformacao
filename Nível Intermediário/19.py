numeros = [2,4,6,8,10,3,5,7,9,11]
soma = 0
qtd = 0

for n in numeros:
    if n % 2 == 0:
        soma += n
        qtd += 1

media = soma / qtd
print(media)
