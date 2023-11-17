'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .'''

t = list(map(int,input().split(" ")))
t[1] += t[0]*60
t[3] += t[2]*60
duracao = (t[3] - t[1])
if duracao <= 0:
    duracao += 24*60

h = duracao//60
m = duracao % 60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,m))