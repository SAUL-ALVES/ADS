#Letra A
celcius=float(input("Digite a temperatura em graus celcius:"))
calculo=(9*celcius+160)/5
print(f"A temperatura em fahrenheit é: {calculo}\n")

#Letra B
f=float(input("Digite a temperatura em graus fahrenheit:"))
calculo1=((f-32)*5)/9
print(f"A temperatura em celsius é: {calculo1}\n")

#Letra C
import math
raio=float(input("Digite o valor do raio da lata de óleo:"))
altura=float(input("Digite a altura da lata de óleo:"))
calculo2=math.pi*raio**2* altura
print(f"O volume da lata de óleo é: {calculo2} cm³\n")

#Letra D
tempo=float(input("Digite o tempo gasto na viagem:"))
velo=float(input("Digite a velocidade media:"))
distancia=tempo*velo
litrosusados= distancia/12
print(f"A quantidade de litros de combustiveis gastos foi: {litrosusados} \nA velocidade media é: {velo} \nA distância percorrida foi {distancia}\n")

#Letra E
print ("Letra E)")
valor=float(input("Digite o valor do bem: "))
taxa=float(input("Digite o valor da taxa: "))
tempo=float(input("Digite o valor do tempo em atraso: "))
prestacao=valor+(valor*(taxa/100)*tempo)
print (f"O valor da prestação do bem em atraso é: {prestacao}\n")

#Letra F
print ("Letra F)")
A=float(input("O valor da variável A é:"))
B=float(input("O valor da variável B é:"))
print (f"Após a troca dos valores ser efetuada, a variável A torna-se: {B} e a variável B, torna-se: {A}\n")

#Letra G
print("Letra G)")
A=int(input("Defina o valor de A: "))
B=int(input("Defina o valor de B: "))
C=int(input("Defina o valor de C: "))
D=int(input("Defina o valor de D: "))
print (f"O progama feito considerando as variáveis no conceito de adição é:\n")

print (f"A + B = {A + B}")
print (f"A + C = {A + C}")
print (f"A + D = {A + D}")
print (f"B + C = {B + C}")
print (f"B + D = {B + D}")
print (f"C + D = {C + D} \n")

print (f"O mesmo progama aplicado a operação de multiplicação é:\n")

print (f"A x B = {A * B}")
print (f"A x C = {A *C}")
print (f"A x D = {A * D}")
print (f"B x C = {B * C}")
print (f"B x D = {B * D}")
print (f"C x D = {C * D} \n")

#Letra H
print ("Letra H)")
comprimento=float(input("Digite o valor do comprimento da caixa:"))
largura=float(input("Digite o valor da largura da caixa:"))
altura=float(input("Digite o valor da altura da caixa:"))
volume=comprimento*largura*altura
print (f"O volume da caixa é igual a: {volume}\n")

#Letra I
print ("Letra I)")
numero=int(input("Digite o valor de um número inteiro:"))
numero_ao_quadrado= numero**2
print (f"O valor do número elevado ao quadrado é: {numero_ao_quadrado}\n")

#Letra J
print ("Letra J)")
A=int(input("Digite um valor no qual representará a variável A:"))
B=int(input("Digite um valor no qual representará a variável B:"))
diferenca= (A - B)**2
print (f"O valor do quadrado da diferença é: {diferenca}\n")

#Letra K
print ("Letra K)")

cotacao_dolar=float(input("Digite o valor da cotação do dólar atualmente:"))
dolar=float(input("Digite a qauntidade de dólares:"))
calc= dolar * cotacao_dolar
print (f"O valor do dólar convertido é: R$ {calc}\n")

#Letra L
print ("Letra L)")

dolar_cotacao=float(input("Digite o valor da cotação do dólar:"))
real=float(input("Digite o valor da quantidade de reais disponível:"))
calculo= real/dolar_cotacao
print (f"O valor em dólar é: US$ {calculo}\n")

#Letra M
print ("Letra M)")

print ("Determine o valor de um número inteiro para as seguintes variáveis:\n")

A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
("\n")
calc1= (A**2) + (B**2) + (C**2)

print (f"O resultado final da soma dos três quadrados é: {calc1}\n")

#Letra N
print ("Letra N)")

print ("Determine o valor de um número inteiro para as seguintes variáveis:\n")

A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
("\n")
calc2= A + B + C
calc3= calc2**2

print (f"O valor do quadrado da soma dos três valores é: {calc3}\n")

#Letra O
print ("Letra O)")

print ("Determine o valor de um número inteiro para as seguintes variáveis:\n")

A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
D=int(input("D"))
("\n")

P= A * C
S= B + D
("\n")

print (f"O resultado do produto do primeiro valor com o terceiro é: {P}, e o resultado da soma do segundo com o quarto é: {S}\n")

#Letra P
print ("Letra P)")

SM=float(input("Digite o valor do seu salário mensal:"))
PR=float(input("Qual o percentual do reajuste?"))
NS= (SM * (PR/100)) + SM

print (f"O valor do novo salário com aumento é: R${NS}\n")

#Letra Q
print ("Letra Q)")

R=float(input("Digite o valor do raio dessa circunferência: "))
A= 3.14*(R**2)
print (f"O valor da área dessa circunferência é: {A}\n")

#Letra R
print ("Letra R)")

A=float(input("Qunatidade de votos do candidato A:"))
B=float(input("Qunatidade de votos do candidato B:"))
C=float(input("Qunatidade de votos do candidato C:"))
nulos=float(input("Quantidade de votos nulos:"))
brancos=float(input("Quantidade de votos em branco:"))
("\n")
total= A + B + C + nulos + brancos
print (f"O valor total de eleitores é: {total}")
perc1= ((A + B + C)/total)*100
print (f"O percentual da quantidade de votos válidos em relação à qauntidade de eleitores é: {perc1}\n")
perc2= (A/total)*100
print (f"O percentual da quantidade de votos do candidato A em relação à qauntidade de eleitores é {perc2}\n")
perc3= (B/total)*100
print (f"O percentual da quantidade de votos do candidato B em relação à qauntidade de eleitores é {perc3}\n")
perc4= (C/total)*100
print (f"O percentual da quantidade de votos do candidato C em relação à qauntidade de eleitores é {perc4}\n")
perc5= (nulos/total)*100
print (f"O percentual da quantidade de votos nulos em relação à qauntidade de eleitores é {perc5}\n")
perc6= (brancos/total)*100
print (f"O percentual da quantidade de votos brancos em relação à qauntidade de eleitores é {perc6}\n")

#Letra S
print ("Letra S)")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
("\n")
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print(f"A soma de {a} e {b} é igual a: {soma}")
print(f"A subtração de {a} por {b} é igual a: {subtracao}")
print(f"A multiplicação de {a} por {b} é igual a: {multiplicacao}")
print(f"A divisão de {a} por {b} é igual a: {divisao}\n")

#Letra T
print("Letra T)")

distancia=float(input("Digite a distância percorrida pelo projétil em km:"))
tempo=float(input("Digite o tempo alcançado pelo projétil em minutos:"))
velocidade= (distancia*1000) / (tempo*60)
print(f"A velocidade alcançada em metros por segundo pelo projétil foi: {velocidade} m/s \n")

#Letra U
print ("Letra U)")

raio=float(input("Digite o valor do raio dessa esfera:"))
volume= (4/3) * 3.14 * (raio**3)
print (f"O volume dessa esfera é: {volume}\n")

#Letra V
print ("Letra V")

base=int(input("Digite o valor da base:"))
expoente=int(input("Digite o valor do expoente:"))
result= base**expoente
print (f"O resultado da potenciação é: {result}\n")

#Letra W
print ("Letra W)")

pe=float(input("Digite a medida em pés:"))
metros= pe * 0.3048
print (f"O valor convertido de pés em metros é: {metros}\n")

#Letra X
print ("Letra X)")

base = float(input("Digite a base da raiz: "))
indice = float(input("Digite o índice da raiz: "))
resultado = base ** (1 / indice)
print(f"A raiz de índice {indice} de base {base} é : {resultado}\n")

#Letra Y
print ("Letra Y)")

nmr=int(input("Digite um número:"))
antecessor= nmr - 1
sucessor= nmr + 1
print (f"O antecessor do número é: {antecessor} e o sucessor é: {sucessor}\n")

#Letra Z
print ("Letra Z)")

A=int(input("Digite um valor numérico inteiro:"))
B=int(input("Digite um valor numérico inteiro:"))
result= (A / B) ** 2
print (f"O quadrado da divisão de {A} por {B} é: {result}")
