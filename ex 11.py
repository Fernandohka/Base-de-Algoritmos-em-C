# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/EX2.c

somaNotas = 0
alunos = 0
media = 0
alunosA = 0
alunosE = 0


print("DIGITE SUA IDENTIFICAÇÃO PARA INFORMAR AS NOTAS OU 0 PARA SAIR\n");

num_id = int(input("Qual o número de identificção: "))

while num_id > 0:
    for i in range(12):
        nota = float(input(f"Qual sua {i+1}ª nota(de 0 a 100): "))
        somaNotas += nota
    
    alunos += 1
    media = somaNotas / 12
    
    print(f"Sua ID é {num_id}")
    print(f"Sua média é = {media:.2f}")
    
    if media >= 90:
        alunosA += 1
        print("Conceito = A")
    elif media >= 75:
        print("Conceito = B")
    elif media >= 60:
        print("Conceito = C")
    elif media >= 40:
        print("Conceito = D")
    else:
        alunosE += 1
        print("Conceito = E")
        
    print("DIGITE SUA IDENTIFICAÇÃO PARA INFORMAR AS NOTAS OU 0 PARA SAIR\n");

    num_id = int(input("Qual o número de identificção: "))
    
    somaNotas = 0

print(f"{alunos} aluno(s) calculados")
print(f"{alunosA} aluno(s) tiraram A")
print(f"{alunosE} aluno(s) tiraram E")