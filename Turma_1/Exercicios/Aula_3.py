#Faça um programa que receba um numero e diga quatas centenas, dezenas e unidades ele tem

valor = input("digite um numero de 0 a 999: \n")
numero = int(valor)
digitos = len(valor)

milhar = (numero//1000)
resto = numero%1000
resposta = ""
if (milhar > 0):
    if(milhar == 1):
        print(milhar,"unidade de milhar")
        resposta = (str(milhar)+" unidade de milhar \n")
    else: 
        print(milhar,"unidades de milhar")
        resposta += (str(milhar)+" unidades de milhar \n")
centena = resto//100
resto = numero%100
if (centena > 0):
    if(centena == 1):
        print(centena,"centena")
        resposta = (str(centena)+" centena \n")
    else: 
        print(centena,"centenas")
        resposta += (str(centena)+" centenas \n")
dezena = resto//10
if (dezena > 0):
    if (dezena == 1):
        print(dezena,"dezena")
        resposta += (str(dezena)+" dezena \n")
    else: 
        print(dezena,"dezenas")
        resposta += (str(dezena)+" dezenas \n")
unidade = resto%10
if (unidade > 0):
    if(unidade == 1):
        print(unidade,"unidade")
        resposta += (str(unidade)+" unidade \n")
    else: 
        print(unidade,"unidades")
        resposta += (str(unidade)+" unidades \n")

print(resposta)
input()


'''

milhar = int(numero//1000)
resto = numero%1000
centena = resto//100
if (milhar > 0):
    if(milhar == 1):
        print(milhar,"unidade de milhar")
        resposta = (milhar,"unidade de milhar")
    else: 
        print(milhar,"unidades de milhar")
        resposta += (milhar,"unidades de milhar")

if (digitos == 3):
    centena = int(numero//100)
elif (digitos == 2):
    dezena = int(numero//10)
    if (centena ==1):
        print(centena,"centena")
    else: print(centena,"centenas")
elif (digitos == 2):
    centena = int(numero/10)
'''    

'''
valor = input("digite um numero: \n")
numero = int(valor)
digitos = len(valor)
centena = int(numero/100)
dezena = int(numero/10)
unidade = numero%10
if centena>0:
    resposta = (str(centena)+"centenas")
if dezena>0:
    resposta += (str(dezena)+"centenas")
if unidade>0:
    resposta += (str(unidade)+"unidades")
print(resposta)


if (digitos == 3):
    centena = int(numero/100)
elif (digitos == 2):
    dezena = int(numero/10)
    if (centena ==1):
        print(centena,"centena")
    else: print(centena,"centenas")
elif (digitos == 2):
    centena = int(numero/10)
 
input()

'''   