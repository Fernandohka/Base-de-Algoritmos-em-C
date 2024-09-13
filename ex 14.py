# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/EX_02.c


def calcula(n1, n2):
    global soma
    global multi
    
    soma = n1 + n2
    multi = n1 * n2
    
    if soma % 2 == 0:
        return 'P'
    else:
        return 'I'

n1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
n2 = int(input("DIGITE O SEGUNDO NUMERO: "))
soma = 0
multi = 0
resp = 0

resp = calcula(n1, n2)

print(f"A soma dos 2 números informados é = {soma}.")
print(f"A multipicação dos 2 números informados é = {multi}.")
print(f"{resp}")