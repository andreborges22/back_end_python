valor = input("digite um numero: \n")
numero = int(valor)
digitos = len(valor)

centena = int(numero/100)
resto = numero%100
if (centena > 0):
    if(centena == 1):
        print(centena,"centena")
        resposta = (centena,"centena")
    else: 
        print(centena,"centenas")
        resposta += (centena,"centenas")
dezena = int(resto/10)
if (dezena > 0):
    if (dezena == 1):
        print("e",dezena,"dezena")
        resposta += ("e",dezena,"dezena")
    else: 
        print("e",dezena,"dezenas")
        resposta += ("e",dezena,"dezenas")
unidade = resto%10
if (unidade > 0):
    if(unidade == 1):
        print("e",unidade,"unidade")
        resposta += ("e",unidade,"unidade")
    else: 
        print("e",unidade,"unidades")
        resposta += ("e",unidade,"unidades")

print(resposta)
input()
'''
if (digitos == 3):
    centena = int(numero/100)
elif (digitos == 2):
    dezena = int(numero/10)
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