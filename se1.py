# 0 - 40 = Reprovado
# 40.1 - 59.9 = Recuperacao
# 60 - 100 = Aprovado
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1+nota2+nota3)/3
print(f"A Media e: {media}")

if(media<=40):
    print("Reprovado!")
elif(media>=60):
    print("Aprovado")
else:
    print("Recuperacao")        