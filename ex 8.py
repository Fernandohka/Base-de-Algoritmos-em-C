# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/sistematabuadas.c

print("SISTEMA DE TABUADAS")

num_tabuada = int(input("Digite o número da tabuada que gostaria de consultar: "))

print(f"{num_tabuada} foi o numero digitado.")

while num_tabuada > 0:
    for i in range(10):
        print(f"{i + 1:2} X {num_tabuada} = {num_tabuada * (i + 1)}")
    
    num_tabuada = int(input("\nDigite o número da tabuada que gostaria de consultar(0 para sair): "))
    print(f"{num_tabuada} foi o numero digitado.")