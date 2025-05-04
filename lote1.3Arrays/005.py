#5. Criar e coletar em um vetor [20] inteiro. Calcule e exiba, segundo:
#10
#∑ (A[1] – A[21–1])
#i = 1

#Função para a coleta de dados para o array:
def coletar_dados(vt):
    for i in range(6):
        vt.append(int(input("Digite o {}º valor: ".format(i + 1))))
    return vt

#Procedimento para cacular e mostrar o requerimento:
def calcular_dados_exibir(vt):
    for inicio in range(len(vt)):
        fim = 5 - inicio
        print("{} - {} ==> {}.".format(vt[inicio], vt[fim], vt[inicio] - vt[fim]))

#Principal:
vt = []
vt = coletar_dados(vt)
calcular_dados_exibir(vt)