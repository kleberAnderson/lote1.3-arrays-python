def carregar_matriz(matriz):
    for i in range(8):
        linha = []
        for j in range(8):
            linha.append(1)
        matriz.append(linha)
    z = 1
    while z <= 4:
        for l in range(z, 8 - z):
            for c in range(z, 8 - z):
                matriz[l][c] = z + 1
        z +=1
    return matriz

def mostrar_matriz(matriz):
    for linha in range(8):
        print(matriz[linha])

matriz = []
opc = 0
while opc != 9:
    opc = int(input(" 1 - Carregar Matriz\n 2 - Mostrar Matriz\n 9 - Sair\n Digite: "))
    match opc:
        case 1:
             matriz = carregar_matriz(matriz)
        case 2: (
            mostrar_matriz(matriz))
        case 9:
            print("\nFim.\n")
        case _:
            print("\nOpção inválida\n!")