a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")

#Antes da Troca
print(f"Antes da Troca: A={a} e B={b}")

c = a # a=10 b=5 c=10
a = b # a=5 b=5 c=10
b = c #a=5 b=10 c=10

print(f"Depois da Troca: A={a} e B={b}")