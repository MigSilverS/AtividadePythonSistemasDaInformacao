# 27. Mediana da lista
numeros = [7, 1, 3, 9, 5, 6, 2, 8, 4, 10]
numeros.sort()
n = len(numeros)
if n % 2 == 0:
    mediana = (numeros[n//2 - 1] + numeros[n//2]) / 2
else:
    mediana = numeros[n//2]
print("Mediana:", mediana)