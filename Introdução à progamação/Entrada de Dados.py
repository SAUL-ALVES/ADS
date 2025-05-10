#questão1
num=int(input("digite um numero iteiro:"))
num2=int(input("digite outro numero iteiro:"))
soma= (num+num2)
print(f"A  soma dos dois numeros inteiros é:{soma}")

#questao2
metros=float(input("Digite a quantidade de metros:"))
calculo= (metros*1000)
print(f"A quantidade de metros em milímetros é {calculo}")

#questao3
dias=int(input("digite a quantidade de dias:"))
horas=int(input("Digite a quantidade de horas:"))
minutos=int(input("Digite a quantidad de minutos:"))
segundos=int(input("digite a quantidade de segundos:"))
diasx=(dias*86400)
horasx= (horas*3600)
minutosx= (minutos*60)
total=(diasx+horasx+minutosx+segundos)
print(f"A quantidade em segundos no geral é: {total}")

#questao4
salario=float(input("Digite o valor do salário:"))
porc=float(input("digite a porcentagem de aumento:"))
aumento= ((salario*porc)/100)
total=(salario+aumento)
print(f"O salario com aumento será: {total}")

#questão5
preço=float(input("Digite o preço da mercadoria:"))
porcdesc=float(input("digite a porcentagem de desconto:"))
desconto= ((preço*porcdesc)/100)
total3=(preço-desconto)
print(f"O preço com desconto será: {total3}R$\n o desconto foi de {desconto} R$")
