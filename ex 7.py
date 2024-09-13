# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/whilepratica06.c


contTotal = 0
contIA = 0
contIB = 0
contJA = 0
contJB = 0
contADUL = 0

idade = int(input("Qual a idade do nadador? "))

while idade > 0:
    if idade >= 18:
        contADUL += 1
        contTotal += 1
        print("Adulto")
    elif idade >= 14:
        contJB += 1
        contTotal += 1
        print("Juvenil B")
    elif idade >= 11:
        contJA += 1
        contTotal += 1
        print("Juvenil A")
    elif idade >= 8:
        contIB += 1
        contTotal += 1
        print("Infantil B")
    elif idade >= 5:
        contIA += 1
        contTotal += 1
        print("Infantil A")
    
    idade = int(input("Qual a idade do nadador? "))

print(f"Categoria infaltil A sao: {contIA}")
print(f"Categoria infaltil B sao: {contIB}")
print(f"Categoria juvenil A sao: {contJA}")
print(f"Categoria juvenil B sao: {contJB}")
print(f"Categoria Adultos sao: {contADUL}")

print(f"total: {contTotal}")