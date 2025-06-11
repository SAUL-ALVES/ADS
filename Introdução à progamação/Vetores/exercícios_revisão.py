

#Atividade - Vetores

#Exercícios de Revisão

#Questão 7

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = []

for i in range(len(A)):
    if i % 2 == 0:
        B.append(A[i] * 5)
    else:
        B.append(A[i] + 5)
print("Vetor A:", A)
print("Vetor B:", B)


#Questão 8

A = [1, 2, 3, 4, 5]
soma = 0

for elemento in A:
    if elemento % 2 != 0:
        soma += elemento
print(soma)

#Questão 9

A = []
contador = 0

while contador < 10:
    nome = str(input("Digite seu nome: "))
    A.append(nome)
    contador += 1
print (A)

#Questão 10

A = [1, 2, 3, 4, 5, 6, 7, 8]
B = []
contador = 0
for i in range(8):
    B.append(A[contador] * 3)
    contador += 1
print (A)
print (B)

#Questão 11

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
C = []

for i in range(20):
    C.append(A[i] - B[i])
print("Os elementos do vetor C são:")
for i in range(20):
    print(f"C[{i}] = {C[i]}")  

#Questão 12

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
B = []
for e in range(15):
    B.append(A[e] ** 2)
print (A)    
print (B)


#Questão 13

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
B = []



for num in A:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    B.append(fatorial)
print (f"Vetor A: ", A)    
print (f"Vetor B: ", B)


#Questão 14

A = list(range(1, 16))
B = list(range(16, 31))
C = A + B
print (C)

#Questão 15

A = list(range(1, 11))
B = []
for i in range(10):
    B.append(A[9 - i])

print("Vetor A:", A)
print("Vetor B:", B)

# Questão 16
A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]
C = [11, 12, 13, 14, 15]
D = []

for i in range(5):
    D.append(A[i])
for i in range(5):
    D.append(B[i])
for i in range(5):
    D.append(C[i])

print("Vetor D (junção de A, B e C):", D)

# Questão 17
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = []

for i in range(10):
    soma = 0
    for j in range(1, A[i] + 1):
        soma += j
    B.append(soma)

print("Vetor A:", A)
print("Vetor B:", B)

# Questão 18
A = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
B = []

for i in range(10):
    B.append(-A[i])

print("Vetor A:", A)
print("Vetor B:", B)

# Questão 19
A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
B = []

for i in range(10):
    B.append(A[i] / 2)

print("Vetor A:", A)
print("Vetor B:", B)

# Questão 20
valor = 5
A = []

for i in range(1, 11):
    A.append(valor * i)

print(f"Tabuada de {valor}: {A}")

# Questão 21
A = [23.5, 24.0, 22.1, 21.5, 23.3, 25.1, 26.2, 24.8, 22.9, 24.7]

menor = A[0]
maior = A[0]
soma = 0

for i in range(10):
    if A[i] < menor:
        menor = A[i]
    if A[i] > maior:
        maior = A[i]
    soma += A[i]

media = soma / 10

print(f"Menor temperatura: {menor}")
print(f"Maior temperatura: {maior}")
print(f"Média das temperaturas: {media}")

# Questão 22
A = [30.0, 25.0, 27.5, 20.0, 22.0]
B = []

for i in range(5):
    B.append(A[i] * 9/5 + 32)

print("Temperaturas em Celsius (A):", A)
print("Temperaturas em Fahrenheit (B):", B)

# Questão 23
A = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
B = []

for i in range(10):
    if A[i] % 2 != 0:
        B.append(A[i] * 2)
    else:
        B.append(A[i])

print("Vetor A:", A)
print("Vetor B:", B)

# Questão 24
A = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]
B = []

for i in range(10):
    if i % 2 == 0:
        B.append(A[i] / 2)
    else:
        B.append(A[i] * 1.5)

print("Vetor A:", A)
print("Vetor B:", B)

# Questão 25
A = [1, 2, 3, 4, 5, 6]
B = [7, 8, 9, 10, 11, 12]
C = []
D = []

for i in range(6):
    if i % 2 != 0:
        C.append(A[i])
        C.append(B[i])
    else:
        D.append(A[i])
        D.append(B[i])

print("Vetor C (índices ímpares):", C)
print("Vetor D (índices pares):", D)

# Questão 26
A = [2, 4, 6, 8, 10, 12]
B = [1, 3, 5, 7, 9, 11]
C = []

for i in range(6):
    C.append(A[i])
    C.append(B[i])

print("Vetor C (junção de A e B):", C)

# Questão 27
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0

for i in range(10):
    if A[i] % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

# Questão 28
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
C = []

for i in range(10):
    C.append((A[i] + B[i]) ** 2)

print("Vetor C:", C)

# Questão 29
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0

for i in range(10):
    if A[i] % 2 == 0:
        pares += 1
    else:
        impares += 1

total = len(A)
percentual_pares = (pares / total) * 100
percentual_impares = (impares / total) * 100

print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")
print(f"Percentual de pares: {percentual_pares}%")
print(f"Percentual de ímpares: {percentual_impares}%")







