# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listacondicional1.c

nome = input("Qual seu nome? ")

idade = int(input("Qual sua idade? "))

sexo = input("Informe seu sexo(M-masculino / F-feminino): ")

print(f"O nome fornecido foi: {nome}")
print(f"A idade fornecida foi: {idade}")
print(f"O sexo informado foi: {sexo}")

if sexo == 'M' and idade >= 18 and idade <= 65:
    print(f"{nome} , está compreendido(a) entre 18 e 65 anos de idade e é do sexo masculino.")
else:
    print(f"{nome} ,ou não está entre 18 e 65 anos de idade e/ou não é masculino.")