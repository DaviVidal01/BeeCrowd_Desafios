'''Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.'''
n1,n2,n3 = map(int, input().split())

valores = [n1,n2,n3]
ordem = sorted(valores)
print(*ordem)