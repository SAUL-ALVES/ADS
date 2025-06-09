#Revisao prova 2

print ("Questão 1\n")

'''
Elabore um programa que leia dois valores numéricos reais desconhecidos.
Em seguida, o programa deve efetuar a adição dos dois valores lidos e apresentar o
resultado caso o mesmo seja maior que 10.
'''

num1 = int(input("Digite o valor de um número, do conjunto dos números reais: "))
num2 = int(input("Digite o valor de outro número, do conjunto dos números reais: "))
calc = num1 + num2
if calc > 10:
    print (f"O resultado da adição é: {calc}\n")


print ("Questão 2\n")

'''
Elabore um programa que leia dois valores numéricos reais desconhecidos.
Em seguida, o programa deve efetuar a adição dos dois valores lidos e caso seja o resultado
maior ou igual a 10, deve ser somado 5. Caso contrário, o valor do resultado deve ser
subtraído de 7. Após a obtenção de um dos novos resultados o novo resultado deve ser
apresentado.
'''
   
num1 = int(input("Digite o valor de um número, do conjunto dos números reais: "))
num2 = int(input("Digite o valor de outro número, do conjunto dos números reais: "))
calc = num1 + num2
if calc >= 10:
    calc1 = calc + 5
    print (f"O resultado é maior ou igual a dez, então: {calc1}")
else:    
    calc2 = calc - 7
    print (f"O resultado é menor do que dez, então: {calc2}")
print ("\n")

print ("Questão 3\n")

'''
Desenvolva um programa que solicite a entrada de um valor numérico inteiro
e apresente uma das seguintes mensagens: “você entrou com o valor 1” se for dada a
entrada do valor numérico 1; “você entrou com o valor 2” se for dada a entrada do valor
numérico 2; “você entrou com um valor muito baixo” se for dada a entrada de um valor
numérico menor que 1; ou “você entrou com um valor muito alto” se for dada a entrada de
um valor numérico maior que 2.
'''

int1 = int(input("Digite o valor de um número inteiro: "))
if int1 == 1:
    print ("Você entrou com o valor 1")
elif int1 == 2:
    print ("Você entrou com o valor 2")
elif int1 < 1:
    print ("você entrou com um valor muito baixo!")
elif int1 > 2:
    print ("você entrou com um valor muito alto!")

print ("\n")

print ("Questão 4\n")

'''
Desenvolver um programa que calcule o reajuste de salário de um
colaborador de uma empresa. Considere que o colaborador deve receber um reajuste de
15% caso seu salário seja menor que R$ 500,00. Se o salário for maior ou igual a R$ 500,00,
mas menor ou igual a R$ 1000,00, seu reajuste será de 10%; caso seja ainda maior que R$
1000,00, o reajuste deve ser de 5%.
'''

salario = int(input("Digite o valor do seu salário: "))
if salario < 500:
    calc1 = salario * (15/100) + salario
    print (f"Seu salário recebeu um reajuste de 15%, então você receberá:  R${calc1}")
elif salario >= 500:
    calc2 = salario * (10/100) + salario
    print (f"Seu salário recebeu um reajuste de 10%, então você receberá:  R${calc2}")
elif salario <= 1000:
    calc3 = salario * (10/100) + salario
    print (f"Seu salário recebeu um reajuste de 10%, então você recebrá:  R${calc3}")
elif salario > 1000:
    calc4 = salario * (5/100) + salario
    print (f"Seu salário recebeu um reajuste de 5%, então você recebrá:   R${calc4}")

print ("\n")

print ("Questão 5\n")

'''
Desenvolva um programa que leia um valor numérico entre os valores 1 e 12
e apresente por extenso o nome do mês correspondente ao valor de entrada. Caso sejam
fornecidos valores menores que 1 e maiores que 12, o programa deve apresentar a
mensagem “Valor inválido!”.
'''


valor = int(input("Digite um valor númerico entre 1 e 12: "))
if valor == 1:        
    print ("Janeiro")
elif valor == 2:
    print ("Fevereiro")
elif valor == 3:
    print ("Março")
elif valor == 4:
    print ("Abril")
elif valor == 5:
    print ("Maio")
elif valor == 6:
    print ("Junho")
elif valor == 7:
    print ("Julho")
elif valor == 8:
    print ("Agosto")
elif valor == 9:
    print ("Setembro")
elif valor == 10:
    print ("Outubro")
elif valor == 11:
    print ("Novembro")
elif valor == 12:
    print ("Dezembro")
    
else:
    print ("Valor iválido!")


print ("\n")
    
print ("Questão 6\n")

'''
Desenvolva um programa que leia um valor numérico inteiro que esteja na
faixa de valores entre 20 e 90. O programa deve apresentar a mensagem “O valor está na
faixa permitida!”, caso o valor informado esteja entre 20 e 90. Se o valor estiver fora da
faixa permitida, o programa deve apresentar a mensagem “O valor está fora da faixa
permitida!”.
'''

valor1 = int(input("Digite um valor númerico: "))

if valor1 >= 20 and valor1 <=90:
    print ("O valor está na faixa permitida!")
else:
    print("O valor está fora da faixa permitida!")

print ("\n")


print ("Questão 7\n")

'''
Desenvolver um programa que solicite a entrada do sexo de uma pessoa e
indique se a informação fornecida é ou não válida. Para o sexo MASCULINO informe a
entrada da letra M e para o sexo FEMININO da letra F. Se forem fornecidos os valores M e F,
o programa deve apresentar uma mensagem avisando que o sexo informado é válido. No
entanto, se for fornecido qualquer outro valor, o programa deve informar que o sexo
fornecido é inválido.
'''

sexo = input("Digite a letra inicial conforme seu sexo: ")

if sexo == "M" or sexo == "m":
    print ("O sexo informado é válido!")
elif sexo == "F" or sexo == "f":
    print ("O sexo informado é válido!")
else:
    print ("O sexo informado é inválido!")


print ("\n")


print ("Questão 8\n")

'''
Elaborar um programa que leia três valores numéricos inteiros, sendo dois
representados pelas variáveis A e B e que serão utilizados para a elaboração de um de dois
cálculos programados: A + B e A – B. O terceiro representado pela variável X será um valor
chave de seleção da operação a ser efetuada. Se o valor da variável X não for maior que 5,
será realizada a operação C = A + B; caso contrário, deve ser realizada a operação C = A – B.
Ao final, o programa deve apresentar o resultado armazenado na variável C.
'''

A = int(input("Digite o valor de um  número inteiro A: "))
B = int(input("Digite o valor de outro número inteiro B: "))
X = int(input("Digite o valor de outro número inteiro X: "))

C = A + B
C1 = A - B

if X < 5:
    print (f"O valor X não é maior que cinco, logo: {C}")
else:
    print (f"O valor X é maior que cinco, logo: {C1}")
    
print ("\n")
print ("Questão 9\n")

valor = float(input("Informe um valor numérico real não negativo: "))


if valor >= 0:
  
    if valor != 5:
        
        resultado = valor ** 0.5
        print(f"A raiz quadrada de {valor} é {resultado:.2f}")
    else:
       
        resultado = valor ** (1/3)
        print(f"A raiz cúbica de {valor} é {resultado:.2f}")
    
print ("\n")


print ("Questão 10\n")


peso1 = float(input("Informe o primeiro peso: "))
peso2 = float(input("Informe o segundo peso: "))
peso3 = float(input("Informe o terceiro peso: "))


if peso1 >= peso2 and peso1 >= peso3:
    maior_peso = peso1
elif peso2 >= peso1 and peso2 >= peso3:
    maior_peso = peso2
else:
    maior_peso = peso3


print(f"O maior peso fornecido é: {maior_peso:.2f}")


print ("\n")


print ("Questão 11\n")


lado_a = float(input("Informe o lado A do triângulo: "))
lado_b = float(input("Informe o lado B do triângulo: "))
lado_c = float(input("Informe o lado C do triângulo: "))


if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    
    if lado_a == lado_b == lado_c:
        print("Os lados formam um triângulo equilátero.")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Os lados formam um triângulo isósceles.")
    else:
        print("Os lados formam um triângulo escaleno.")
else:
    print("Os lados fornecidos não formam um triângulo.")

