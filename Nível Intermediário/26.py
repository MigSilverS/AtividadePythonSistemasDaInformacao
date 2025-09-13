# 26. Remover strings com 'a'
palavras = ["python", "java", "c", "ruby", "perl", "swift"]
sem_a = []
for p in palavras:
    if "a" not in p.lower():
        sem_a.append(p)
print("Sem 'a':", sem_a)