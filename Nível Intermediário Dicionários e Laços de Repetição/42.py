# 42. Média de notas dos alunos
alunos = {"João": [8.5, 9.0], "Maria": [7.0, 6.5], "Ana": [10, 9], "Pedro": [5, 6]}
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome} -> média {media:.2f}")