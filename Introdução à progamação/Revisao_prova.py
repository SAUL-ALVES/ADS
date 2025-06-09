#Questão 6
print ("Questão 6\n")

salario = float(input("Digite o valor do salário base: "))
gratifc = salario * 0.05
imp = salario * 0.07
salario_receber = salario + gratifc - imp
print (f"O salario com a gratificação e o imposto pago é: {salario_receber}\n")


#Questão 7

print ("Questão 7\n")

salario_base = float(input("Digite o salário base do funcionário: R$ "))
gratificacao = 50.00
imposto = 0.10 * salario_base
salario_receber = salario_base + gratificacao - imposto

print(f"O salário a receber é: R$ {salario_receber:}\n")

#Questão 8
print ("Questão 8\n")

valord = float(input("Digite o valor depositado: "))
juros = float(input("Digite o valor da taxa de juros em (%): "))
rendimento = valord * (juros/100)
total = rendimento + valord
print (f"O valor do rendimento é: {rendimento}")
print (f"O valor total depois do rendimento é: {total}\n")

#Questão 9
print ("Questão 9\n")

base = float(input("Digite o valor da base de um triângulo: "))
altura = float(input("Digite o valor da altura desse mesmo triângulo: "))
area = (base*altura)/2
print (f"O valor da área do triângulo é: {area}\n")

#Questão 10
print ("Quetão 10\n")

pi = 3.14
raio = float(input("Digite o valor do raio: "))
area = pi * (raio**2)
print (f"O valor da área desse circulo é: {area}\n")


#Questão 11
print ("Questão 11\n")

positivo = float(input("Digite o valor de um número positivo maior que zero: "))
if  positivo > 0:
    quadrado = positivo ** 2
    cubo = positivo ** 3
    raiz = positivo ** 0.5
    cubica = positivo ** (1/3)

    print (f"O valor do número ao quadrado é: {quadrado}")
    print (f"O valor do número ao cubo é: {cubo}")
    print (f"O valor da raiz quadrada do número é: {raiz}")
    print (f"O valor da raiz cúbica do número é: {cubica}")
else:
    print ("Erro. Digite um número maior do que zero")
    



#Questão 12
print ("\n")
print ("Questão 12\n")
 
    
num1 = float(input("Digite um valor maior que zero: "))
num2 = float(input("Digite outro valor maior que zero: "))
calc = num1 ** num2
print (f"O valor dos dois números ao quadrado é: {calc}\n")

   
#Questão 13
print ("Questão 13\n")

nasc = int(input("Digite a data do seu ano de nascimento: "))
atual = int(input("Digite o valor do ano atual em que estamos: "))
idade = atual - nasc
futuro = 2050 - nasc
print (f"A sua idade é: {idade}")
print (f"Você terá essa idade em 2050: {futuro}\n")


#Questão 14

print ("Questão 14\n")

precofab = int(input("Digite o valor do preço de fábrica do carro: "))
perc = int(input("Digite o valor do percentual de lucro do distribuidor em porcentagem: "))
percimp = int(input("Digite o valor do percentual do imposto, em porcentagem: "))

lucrodis = (precofab * (percimp/100)) + precofab
imp = precofab * (percimp/100)
final = lucrodis + imp

print (f"O valor correspondente ao lucro do distribuidor é: {lucrodis}")
print (f"O valor dos impostos são: {imp}")
print (f"O preço final do veículo é: {final}\n")



#Questão 15

print ("Questão 15\n")

trabalhadasmes = int(input("Digite o valor de horas trabalhadas no mês: "))
salariomin = float(input("Digite o valor do salário mínimo: "))
trabalhadadia = salariomin ** 1/2
bruto = trabalhadadia * trabalhadasmes
imp = (3/100) * bruto
receber = bruto - imp

print (f"O salário a receber é equivalente a: {receber}")

  


