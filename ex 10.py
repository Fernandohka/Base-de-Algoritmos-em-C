# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/EX1.c

hora = 10.00
horaExtra = 15.00

horas_normais = float(input("Informe o numero de horas normais trabalhadas no ano: "))

horas_extras = float(input("Informe o numero de horas extras trabalhadas no ano: "))

horasnorm_resul = horas_normais * hora
horasext_resul = horas_extras * horaExtra
resul = horasnorm_resul + horasext_resul

poup = resul * 0.08

print(f"Valor de horas normais: {horasnorm_resul:.2f} reais")
print(f"Valor de horas extras: {horasext_resul:.2f} reais")
print(f"Total de ganho no ano = {resul:.2f} reais")
print(f"Valor a guardar na poupança = {poup:.2f} reais")