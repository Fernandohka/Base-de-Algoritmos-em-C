# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/somade2matrizes.c

mat1 = [[0,0,0], [0,0,0], [0,0,0]]
mat2 = [[0,0,0], [0,0,0], [0,0,0]]
matsoma = [[0,0,0], [0,0,0], [0,0,0]]

print("PRIMEIRA MATRIZ")
for l in range(3):
    for c in range(3):
        mat1[l][c] = int(input(f"Informe a posição da linha {l}, e da coluna {c} da matriz: "))

print("SEGUNDA MATRIZ")
for l in range(3):
    for c in range(3):
        mat2[l][c] = int(input(f"Informe a posição da linha {l}, e da coluna {c} da matriz: "))
    
for l in range(3):
    for c in range(3):
        matsoma[l][c] = mat1[l][c] + mat2[l][c]

print("SOMA DAS 2 MATRIZES")
for l in range(3):
    for c in range(3):
        print(f"| {matsoma[l][c]} |", end="")
    print()