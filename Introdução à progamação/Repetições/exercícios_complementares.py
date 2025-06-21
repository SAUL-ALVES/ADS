# Repetições  
# Exercícios

# 1.
print("Questão 1")
contador = 1
while contador <= 5:
    num = int(input("Digite o valor de um número inteiro: "))
    mul = num * 3
    print(f"O valor do número multiplicado por 3 é: {mul}")
    contador += 1
print("\n")

# 2.
print("Questão 2")
while True:
    num = int(input("Digite o valor de um número inteiro qualquer: "))
    mul = num * 3
    print(f"O valor do número multiplicado por 3 é: {mul}")
    novo = input("Deseja novo cálculo? (sim/não): ").lower()
    if novo == 'não' or novo == 'nao' or novo == 'Não' or novo == 'Nao':
        print("Programa encerrado!")
        break
print("\n")

# 3.
print("Questão 3")
num = 5
fatorial = 1
contador = 1
while contador <= num:
    fatorial *= contador  
    contador += 1
print(f"O fatorial de {num} é: {fatorial}")
print("\n")

# 4.
print("Questão 4")
num = int(input("Digite o valor de um número qualquer: "))
contador = 1
fatorial = 1
while contador <= num:
    fatorial *= contador 
    contador += 1
print(f"O fatorial de {num} é: {fatorial}")
print("\n")

# 5.
print("Questão 5")
inicio = 15
fim = 200
contador = inicio
while contador <= fim:
    quadrado = contador ** 2
    print(f"O valor do quadrado do número {contador} é: {quadrado}")
    contador += 1
print("\n")

# 6.
print("Questão 6")
acumulador = 0
contador = 1
while contador <= 100:
    acumulador += contador  
    contador += 1
print(f"A soma dos números naturais de 1 a 100 é: {acumulador}")
print("\n")

# 7.
print("Questão 7")
acumulador = 0
contador = 2
while contador <= 500:
    acumulador += contador
    contador += 2
print(f"O somatório dos valores pares entre 1 e 500 é: {acumulador}")
print("\n")

# 8.
print("Questão 8")
contador = 1
while contador <= 20:
    print(f"Os valores ímpares de 0 a 20, são: {contador}")
    contador += 2
print("\n")

# 9.
print("Questão 9")
base = 3
expoente = 0
while expoente <= 15:
    resultado = base ** expoente
    print(f"{base} elevado a {expoente} é: {resultado}")
    expoente += 1
print("\n")

# 10.
print("Questão 10")
base = int(input("Digite a base (valor inteiro): "))
expoente = int(input("Digite o expoente (valor inteiro): "))
resultado = 1
contador = 0
while contador < expoente:
    resultado *= base
    contador += 1
print(f"{base} elevado a {expoente} é: {resultado}")
print("\n")

# 11.
print("Questão 11")
anterior = 0
atual = 1
contador = 2
print(f"{anterior}")
print(f"{atual}")
while contador < 15:
    proximo = anterior + atual
    print(proximo)
    anterior = atual
    atual = proximo
    contador += 1
print("\n")

# 12.
print("Questão 12")
celsius = 10
while celsius <= 100:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
    celsius += 10
print("\n")

# 13.
print("Questão 13")
soma_fatorial = 0
contador_geral = 0
while contador_geral < 15:
    valor = int(input("Digite um valor inteiro: "))
    fatorial = 1
    contador = 1
    while contador <= valor:
        fatorial *= contador
        contador += 1
    soma_fatorial += fatorial
    contador_geral += 1
print(f"Somatório dos fatoriais: {soma_fatorial}")
print("\n")

# 14.
print("Questão 14")
soma = 0
contador = 0
while contador < 10:
    valor = float(input("Digite um valor real: "))
    soma += valor
    contador += 1
media = soma / 10
print(f"Somatório: {soma}, Média: {media}")
print("\n")

# 15.
print("Questão 15")
soma = 0
cont = 0
while True:
    valor = float(input("Digite um valor (negativo para parar): "))
    if valor < 0:
        break
    soma += valor
    cont += 1
if cont > 0:
    media = soma / cont
    print(f"Somatório: {soma}, Média: {media}, Total de valores: {cont}")
else:
    print("Nenhum valor positivo foi inserido.")
print("\n")

# 16.
print("Questão 16")
num = 1
while num <= 10:
    if num % 2 != 0:
        fatorial = 1
        contador = 1
        while contador <= num:
            fatorial *= contador
            contador += 1
        print(f"O fatorial de {num} é {fatorial}")
    num += 1
print("\n")

# 17.
print("Questão 17")
soma = 0
cont = 0
num = 50
while num <= 70:
    if num % 2 == 0:
        soma += num
        cont += 1
    num += 1
media = soma / cont
print(f"Soma dos pares: {soma}, Média: {media}")
print("\n")

# 18.
print("Questão 18")
area_total = 0
while True:
    comodo = input("Digite o nome do cômodo: ")
    largura = float(input(f"Digite a largura do(a) {comodo} em metros: "))
    comprimento = float(input(f"Digite o comprimento do(a) {comodo} em metros: "))
    area = largura * comprimento
    print(f"A área do(a) {comodo} é {area} metros quadrados.")
    area_total += area
    continuar = input("Deseja calcular outro cômodo? (sim/não): ").lower()
    if continuar == 'não':
        break
print(f"A área total da residência é: {area_total} metros quadrados.")
print("\n")

# 19.
print("Questão 19")
valor = int(input("Digite um valor positivo (negativo para parar): "))
maior = valor
menor = valor
while valor >= 0:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    valor = int(input("Digite um valor positivo (negativo para parar): "))
print(f"Maior valor: {maior}, Menor valor: {menor}")
print("\n")
