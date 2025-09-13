lista = ["termo", "coisa", "turne", "grego", "brownie"]

vogais = "aeiouAEIOU"

for palavra in lista:
    contador = 0
    for vogal in palavra:
        if vogal in vogais:
            contador +=1
    print(contador)

