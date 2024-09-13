# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/dadosvetor.c

vetjogo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
valor6 = 0

for i in range(20):
    vetjogo[i] = int(input("Informe o número tirado no dado(de 1 a 6): "))
    
    if vetjogo[i] == 1:
        valor1 += 1
    
    if vetjogo[i] == 2:
        valor2 += 1
        
    if vetjogo[i] == 3:
        valor3 += 1
        
    if vetjogo[i] == 4:
        valor4 += 1
        
    if vetjogo[i] == 5:
        valor5 += 1
        
    if vetjogo[i] == 6:
        valor6 += 1

print(f"Número 1 foi tirado {valor1} vezes.")
print(f"Número 2 foi tirado {valor2} vezes.")
print(f"Número 3 foi tirado {valor3} vezes.")
print(f"Número 4 foi tirado {valor4} vezes.")
print(f"Número 5 foi tirado {valor5} vezes.")
print(f"Número 6 foi tirado {valor6} vezes.")