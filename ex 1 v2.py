# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/recursividade2aula.c

def FAT(p_num):
    if p_num == 0:
        return 1
        
    print(f"{p_num} é um dos numeros.")
    return p_num * FAT(p_num - 1)



num = int(input())

fatorial = FAT(num)

print(f"O fatorial de {num} é: {fatorial}")