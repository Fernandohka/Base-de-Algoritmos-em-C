# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/whilepratica05.c

num_pessoas = 0
resp = 0
sexo = ''

alt = float(input("Qual a altura da pessoa? "))

while alt > 0:
    sexo = input("Qual o sexo da pessoa?(M)Homens/(F)Mulheres ")
    
    num_pessoas += 1
    
    if sexo == 'M':
        resp = (72.7 * alt) - 58
    else:
        resp = (62.1 * alt) - 44.7
    
    print(f"Seu peso ideal é de: {resp:.2f} kilos")
    
    alt = float(input("Qual a altura da pessoa? "))

print(f"{num_pessoas} participantes")