#Criar e coletar um vetor [50] inteiro. Calcular e exibir:
#a. A média dos valores entre 10 e 200;
#b. A soma dos números ímpares.

#Uso de um array de 10 posições para fins de testes:
array = []
soma = 0
for i in range(10):
    array.append(int(input("Digite o {}º valor: ".format(i + 1))))
#requesito a:
contador = 0
for i in array:
    if 10 <= i <= 200:
        soma += i
        contador += 1
print ("Média ==> {}.".format(float(soma / contador)))
#requesito b:
soma = 0
for i in array:
    if i % 2 != 0:
        soma += i
print("Soma dos números ímpares ==> {}".format(soma))
