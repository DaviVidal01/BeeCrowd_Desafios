'''Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

1 Cachorro Quente 4.00
2 X-Salada 4.50
3 X-Bacon 5.00
4 Torrada Simples 2.00
5 Refrigerante 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.'''

c,q = map(float,input().split(" "))
if c == 1:
    print("Total: R$ {:.2f}".format(q*4.0))
elif c == 2:
    print("Total: R$ {:.2f}".format(q*4.50))
elif c == 3:
    print("Total: R$ {:.2f}".format(q*5.0))
elif c == 4:
    print("Total: R$ {:.2f}".format(q*2.0))
elif c == 5:
    print("Total: R$ {:.2f}".format(q*1.50))