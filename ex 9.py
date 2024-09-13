# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/testematriz12.c

DIML = 3
DIMC = 5

matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

for l in range(DIML):
    for c in range(DIMC):
        matriz[l][c] = int(input(f"Informe a posição {l}, {c} da matriz: "))
    
for l in range(DIML):
    for c in range(DIMC):
        print(f"{matriz[l][c]:4}", end="")
    print()