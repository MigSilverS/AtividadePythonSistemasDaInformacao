# 46. Aumento de 10% nos salários
salarios = {"Ana": 2000, "Carlos": 2500, "Maria": 3000, "João": 1500, "Fernanda": 4000}
for nome, salario in salarios.items():
    novo = salario * 1.1
    print(f"{nome}: R$ {novo:.2f}")