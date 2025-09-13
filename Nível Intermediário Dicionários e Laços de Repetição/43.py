# 43. Frequência de letras em uma frase
frase = "programar em python é divertido"
frequencia = {}
for letra in frase.replace(" ", ""):
    frequencia[letra] = frequencia.get(letra, 0) + 1
print("Frequência de letras:", frequencia)