numeros = [1,-3,-23,-33,232,-12,2,3,4,5]
soma = 0

for numero in numeros:
    if numero < 0:
        soma+=numero
        print(soma)

print(soma)
