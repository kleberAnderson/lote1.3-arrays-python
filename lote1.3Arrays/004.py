#4. Criar e coletar em um vetor [30] real e calcular e exibir:
#a. A média do grupo;
#b. A quantidade de notas acima do grupo;
#c. As posições dos valores abaixo da média do grupo.

#Para realização de teste, uso de um vetor de 5 posições
vt = []
for i in range(5):
    vt.append(float(input("Digite o {}º valor: ".format(i + 1))))

#Requesito a:
soma = 0
for i in vt:
    soma += i
media = soma / 5
print("\nMédia do grupo ==> {}.".format(media))

#Requesito b:
notas_acima = 0
for i in vt:
    if i > media:
        notas_acima += 1
print("\nQuantidade de notas acima da média ==> {}.".format(notas_acima))

#Requesito c:
print("\nValores menores que a média: ")
for i in range(5):
    if vt[i] < media:
        print("Valor {}, posição ==> {}".format(vt[i], i))