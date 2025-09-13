# 37. Verificar se 'Python' está nos valores
cursos = {"Curso1": "Java", "Curso2": "Python", "Curso3": "C#"}
for linguagem in cursos.values():
    if linguagem == "Python":
        print("Python encontrado!")