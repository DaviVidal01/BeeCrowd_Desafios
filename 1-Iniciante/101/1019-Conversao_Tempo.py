'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

'''
horas = 0
minutos = 0
segundos = int(input())
if segundos >= 3600:
    horas = segundos // 3600
    segundos = segundos % 3600
if segundos >= 60:
    minutos = segundos // 60
    segundos = segundos % 60
print("{}:{}:{}".format(horas,minutos,segundos))

