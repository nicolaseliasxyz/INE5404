"""

Lista 2:

"""
#Exercicio 1:
lista1 = []
for i in range(0,5):
    n = int(input())
    lista1.append(n)

for i in range(0, 5):
    print(lista1[i])


#Exercicio 2:
lista2 = []
for i in range(0,10):
    n = int(input())
    lista2.append(n)

for i in range(0,10):
    print(lista1[-1 - i])


#Exercicio 3: 
lista3 = []
media_soma = 0
for i in range(0,4):
    n = int(input())
    lista3.append(n)

for i in range(0,4):

    media_soma += lista3[i]

media_final = media_soma / len(lista3)

print(lista3)

print(media_final)


#Exercicio 4:
lista4 = ['q','w','e','r', 't', 'y', 'u', 'i', 'o', 'p']

lista4_consoantes = ['q','w','e','r', 't', 'y', 'u', 'i', 'o', 'p']

lista_suporte = ['a', 'e', 'i', 'o', 'u']

for i in range(0,len(lista4)):
    for j in range(0, 4):
        if lista4[i] == lista_suporte[j]:
            lista4_consoantes.remove(lista4[i])
            break
        
num_consoantes = len(lista4_consoantes)

print(f'Foram lidas {num_consoantes} consoantes')
print(lista4_consoantes)


#Exercicio 5:
vetor_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

vetor_par = []
vetor_impar = []

for i in range(0,len(vetor_num)):
    if vetor_num[i] % 2 == 0:
        vetor_par.append(vetor_num[i])
    else:
        vetor_impar.append(vetor_num[i])
        
        

print(f'Vetor par: {vetor_par}')
print(f'Vetor impar: {vetor_impar}')


#Exercicio 6:
soma = 0
medias = []
medias_maior7 = []

for i in range(0,10):
    soma = 0
    print('Digite 4 Notas sem virgulas separadas por espaço EX: 8 8 8 8')
    n = input().split()#------EXEMPLO DE ENTRADA: 8 8 8 8
    for j in range(0,4):
        soma += int(n[j])
    media = soma / 4
    medias.append(media)
    if media >= 7:
        medias_maior7.append(media)
        

print(len(medias_maior7))


#Exercicio 7:
vetor = [5, 5, 5, 5, 5]

soma_vetor = 0
for i in range(0, 5):
    soma_vetor += vetor[i]

print(soma_vetor)

mult_vetor = vetor[0]
for i in range(0, 5 - 1):
    mult_vetor *= vetor[i]

print(mult_vetor)

print(vetor)


#Exercicio 8:
idades = []
alturas = []

for i in range(0, 5):
    print('Digite um numero inteiro correspondente a idade:')
    idade = int(input())
    idades.append(idade)
for i in range(0, 5):
    print('Digite um numero em ponto flutuante correspondente a altura em metros:')
    altura = float(input())
    alturas.append(altura)
print('idades')
for i in range(0, 5):
    print(idades[-1 -i])
print('alturas')
for i in range(0, 5):
    print(alturas[-1 -i])


#Exercicio 9:
a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
b = []

for i in range(0, 10):
    b.append((a[i]**2))

print(b)


#Exercicio 10:
j = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
k = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

w = []

for i in range(0, 10):
    w.append(j[i])
    w.append(k[i])

print(w)


#Exercicio 11:
j = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
k = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
w = []

for i in range(0, 10):
    w.append(j[i])
    w.append(k[i])
    w.append(y[i])

print(w)













    
    





