#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/3naoentregar.c

def Calcula(p1, p2):
    Aux = 0
    Aux = int(p1) + (int(p1) * float(10/100))
    p2 = int(p1) + (int(p1) * float(20/100))
    p1 = int(p1) + (int(p1) * float(15/100))
    return Aux

def Mostra(p_Sal_10, p_Sal_15, p_Sal_20):
    print(f"O salario 1 é {float(p_Sal_10):.2f}")
    print(f"O salario 2 é {float(p_Sal_15):.2f}")
    print(f"O salario 3 é {float(p_Sal_20):.2f}")

Sal_10 = 0
Sal_15 = 0
Sal_20 = 0

Sal_15 = input("informe: ")

Calcula(Sal_15, Sal_20)
Mostra(Sal_10, Sal_15, Sal_20)