psr = float(input("Saco de Ração Kg: "))
qtd = int(input("Qtd diaria de cada gato gr: "))

#peso SR em Gramas
psr_g = psr*1000

#consumo gatos em 5 dias
consumo_gt = (qtd*2)*5

#Restante do Saco de Ração
res = psr_g - consumo_gt

#Resposta
print(f"Sobrou {res} gr no Saco de Ração")