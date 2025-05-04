#9. Criar e carregar uma matriz [4][4] com valores aleatórios, sendo que a
#diagonal principal terá seus dados carregados no programa segundo:
import random

def carregar_matriz(matriz):
    for linha in range(4):
        l = []
        for coluna in range(4):
            if linha == coluna:
                l.append(4 ** coluna)
            else:
                l.append(random.randint(0, 64))
        matriz.append(l)
    print("\nMatriz carregada!\n")
    return matriz

def mostrar_matriz(matriz):
    for i in range(4):
        print(matriz[i])
matriz = []
opc = 0
while opc != 9:
    opc = int(input(" 1 - Carregar Matriz\n 2 - Mostrar Matriz\n 9 - Sair\n Digite: "))
    match opc:
        case 1:
            matriz = carregar_matriz(matriz)
        case 2:
            mostrar_matriz(matriz)
        case 9:
            print("Fim")
        case _:
            print("\nOpção inválida.\n")