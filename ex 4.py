# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/aulapraticacomandofor05.c

totalsexof21 = 0
totalidadef = 0
totalsexof = 0
totalsexom18 = 0
totalidadem = 0
totalsexom = 0

for i in range(3):
    idade = int(input("Qual a idade: "))
    sexo = input("QUAL O SEXO: ")
    
    if idade >= 21 and sexo == 'F':
        totalsexof21 += 1
        totalidadef += idade
    else:
        if sexo == 'F':
            totalsexof += 1
            totalidadef += idade
    
    if idade >= 18 and sexo == 'M':
        totalsexom18 += 1
        totalidadem += idade
    else:
        if sexo == 'M':
            totalsexom += 1
            totalidadem += idade

mediaf = totalidadef/(totalsexof + totalsexof21)
mediam = totalidadem/(totalsexom + totalsexom18)

print(f"Total do sexo feminio e maior que 21 é de: {totalsexof21}")
print(f"Total do sexo masculino e maior que 18 é de: {totalsexom18}")
print(f"Media de idade do sexo feminino é de: {mediaf:.2f}")
print(f"Media de idade do sexo masculino é de: {mediam:.2f}")