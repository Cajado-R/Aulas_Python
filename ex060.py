"""num = int(input('Digite um número para receber o seu fatorial '))
ls = int
for c in range (num):
    ls = (num-1) * num
    print(num)"""
import math
print(30*'-')
print('VENHA CALCULAR O FATORIAL')
print(30*'-')
soma = 0
num = int(input('Digite um número para recebero fatorial: '))
fato = num
rial = 1
while fato > 0:
   #print que adiciona o número do fatorial primeiro
   print(f'{fato}', end='')
   #print que imprime X caso o número do fatorial seja maior que 1 senão imprime igual
   print(' X ' if fato > 1 else ' = ',end='')
   rial *= fato
   fato -= 1
   resultado = rial
print(f'{resultado}')
