#3. Criar e coletar valores inteiros nos vetores VT1[3] e VT2[3]. Concatenar
#esses valores em um 3º vetor (VT3[6]) e mostrar os seus dados. P. ex:
#VT1| 1| 2| 3|
#|VT2| 4| 5| 6|
#|VT3| 1| 2| 3| 4| 5| 6

vt1 = []
vt2 = []
vt3 = []

for i in range(3):
    vt1.append(int(input("Digite o {}º valor: ".format(i + 1))))
for i in range(3):
    vt2.append(int(input("Digite o {}º valor: ".format(i + 1))))

for i in range(6):
    if i < 3:
        vt3.append(vt1[i])
    else:
        vt3.append(vt2[i - 3])
print("\nVetor 3 ==> {} ".format(vt3))
