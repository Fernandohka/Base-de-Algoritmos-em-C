# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/EX_04.c

def conta(x):
    while x <= 100:
        print(f"{x}")
        x += 1

num = int(input("Informe um número pra ir dele até 100: "))
conta(num)