# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/aulapratica26.c

h1 = float(input("Informe as horas trabalhadas no primeiro dia: "))
h2 = float(input("Informe as horas trabalhadas no segundo dia: "))
h3 = float(input("Informe as horas trabalhadas no terceiro dia: "))
h4 = float(input("Informe as horas trabalhadas no quarto dia: "))
h5 = float(input("Informe as horas trabalhadas no quinto dia: "))

resp = (h1 + h2 + h3 + h4 + h5) / 5

print(f"A média de horas trabalhadas é de: {resp:.2f} horas por dia")