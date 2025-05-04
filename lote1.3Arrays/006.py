#6. Criar e coletar em um vetor [20] com números aleatórios. Classificar este
#vetor em ordem crescente e mostre os dados.

# 7. A partir do exercício 6 (vetor classificado) solicitar um valor qualquer e
# verificar a sua existência no vetor (utilizar pesquisa binária).

#Para realização de teste, uso de um vetor de 5 posições

#Função para coleta de dados:
def coletar_valores(vt):
    for i in range(5):
        vt.append(int(input("Digite o {}º valor: ".format(i + 1))))
    return vt

#Função para classicar o vetor:
def classificar_vetor(vt):
    save = 0
    for i in range(len(vt) - 1):
        for j in range(i + 1, len(vt)):
            if vt[i] > vt[j]:
                save = vt[i]
                vt[i] = vt[j]
                vt[j] = save
    print("\nVetor classificado!")
    return vt

#Função para mostrar o vetor:
def mostrar_vetor(vt):
    print(vt)

def busca_binaria(vet):
    inicio = 0
    fim = len(vet)
    busca = int(input("Digite o valor de busca: "))
    status = False

    while inicio < fim and status == False:
        meio = int((inicio + fim) / 2)
        if busca == vet[meio]:
            status = True
        else:
            if busca < vet[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
    if status:
        print("Valor {} existente!".format(busca))
    elif not status:
        print("Número não existente!")

vt = []
op = 0
while op != 9:
    op = int((input(
        " 1 - Coletar dados para o vetor \n 2 - Classificar em ordem cresecente\n 3 - mostrar vetor\n 4 - Busca Binária\n 9 - Sair\n Digite: ")))
    match op:
        case 1: vt = coletar_valores(vt)
        case 2: vt = classificar_vetor(vt)
        case 3: mostrar_vetor(vt)
        case 4: busca_binaria(vt)
        case 9: print("Fim.")
        case _: print("\nOpção inválido!\n")