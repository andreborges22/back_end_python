#importa a biblioteca datetime, para uso de datas
#import datetime

#Solicitando dados do usuario
dia_nascimento = input("Informe o dia do seu nascimento, com 2 digitos, e em seguida aperte enter\n")
mes_nascimento = input("Informe o mês do seu nascimento, com 2 digitos, e em seguida aperte enter\n")
ano_nascimento = input("Informe o ano do seu nascimento, com 4 digitos, e em seguida aperte enter\n")

#armazenando e imprimindo resultado
resultado = "Você nasceu em "+dia_nascimento+"/"+mes_nascimento+"/"+ano_nascimento
#resultado = "Você nasceu em "+dia_nascimento+"/"+mes_nascimento+"/"+ano_nascimento
print (resultado)

'''
#convertendo dados coletados em um campo datetime
data_aniversario = datetime.date(int(ano_nascimento),int(mes_nascimento),int(dia_nascimento))

#armazenando e imprimindo resultado
resultado = "Você nasceu em "+str(data_aniversario.day)+"/"+str(data_aniversario.month)+"/"+str(data_aniversario.year)
print (resultado)

#coletando a data atual
data_atual = datetime.date.today()
#calculando e imprimindo idade
idade = data_atual - data_aniversario
print (idade)

#calculando e imprimindo idade sem considerar aniversario
idade = int(data_atual.year) - int(ano_nascimento)
print (idade)

#condicional checar aniversario
if data_aniversario<data_atual:
    #se a pessoa ainda nao fez aniversário, a idade sofre um decrécimo
    idade = idade-1
    print("Seu aniversário ainda não chegou")
    print ("Você tem",idade,"anos")
else:
    print("Seu aniversário já chegou")
    print ("Você tem",idade,"anos")
    
'''

input()