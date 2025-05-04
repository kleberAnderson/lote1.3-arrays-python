#2. Criar e coletar um vetor [100] inteiro e exibir:
#a. O maior e o menor valor;
#b. A média dos valores.

#Uso de um array de 10 posições para fins de testes:
array = []
for i in range(10):
    array.append(int(input("Digite o {}º valor: ".format(i + 1))))

#Requesito a:
#Uso da ordenação BubbleSort:
save = 0
for i in range(10):
    for j in range(i + 1, 10):
        if array[i] > array[j]:
            save = array[i]
            array[i] = array[j]
            array[j] = save
print(array)
print("Maior número ==> {}, Menor número ==> {}".format(array[9], array[0]))

#Requesito b:
soma = 0
for i in array:
    soma += i
print("Média dos valores ==> {}".format(soma / 10))