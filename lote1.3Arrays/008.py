#8.Criar e carregar uma matriz [4][3] inteiro com quantidade de produtos
#vendidos em 4 semanas. Calcular e exibir:
#a. A quantidade de cada produto vendido no mês;
#b. A quantidade de produtos vendidos por semana;
#c. O total de produtos vendidos no mês.

#Função para prencher a matriz:
def prencher_dados(matriz):
    for linha in range(4):
        semana = []
        for coluna in range(3):
            produto = int(input("Digite a qtde do {}º produto vendido semana {}: ".format(coluna + 1, linha + 1 )))
            semana.append(produto)
        matriz.append(semana)
    return matriz

#Metodo para mostrar a Matriz:
def mostrar_matriz(matriz):
    for linha in range(4):
        print(matriz[linha])

#Metodo para mostrar a quantidade de cada produto vendido no mês:
def mostrar_qtd_produto(matriz):
    for coluna in range(3):
        soma_produto = 0
        for linha in range(4):
            soma_produto += matriz[linha][coluna]
        print("Produto {} totalizou ==> {} unidades.".format(coluna + 1, soma_produto))

#Metodo para calcular o total de produtos vendidos na semana:
def mostrar_qtd_produto_semana(matriz):
    for linha in range(4):
        soma = 0
        for coluna in range(3):
            soma += matriz[linha][coluna]
        print("total vendido na semana {} ==> {} produtos.".format(linha + 1, soma))

#Metodo para calcular o total de produtos vendidos no mês:
def cacular_total(matriz):
    total = 0
    for linha in range(4):
        for coluna in range(3):
            total += matriz[linha][coluna]
    return print("Total de produtos vendidos no mês ==> {} unidades.".format(total))

#Principal:
matriz = []
opc = 0
while opc != 9:
    opc = int(input(" 1 -Preencher matriz\n 2 - Mostrar Matriz\n 3 - Mostrar qtde produto vendido\n 4 - Mostrar qtde vendido na semana\n 5 - Mostrar a qtde vendida no mês\n 9 - Fim\n Digite opção:  "))
    match opc:
        case 1:
            matriz = prencher_dados(matriz)
        case 2:
            mostrar_matriz(matriz)
        case 3:
            mostrar_qtd_produto(matriz)
        case 4:
            mostrar_qtd_produto_semana(matriz)
        case 5:
            cacular_total(matriz)
        case 9:
            print("Fim!")
        case _:
            print("Opção inválida!")