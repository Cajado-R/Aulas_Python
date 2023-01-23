print(30*'-')
print('VAMOS CALCULAR O FATORIAL')
print(30*'-')
n = int(input('Digite um número para obter a sequência fibonacci: '))
fato = n
rial = 1
print('Sabendo que o valor de n é 4 obteremos o seguinte resultado:' )
while fato > 0:
   #print que adiciona o número do fatorial primeiro
   print(f'{fato}', end='')
   #print que imprime X caso o número do fatorial seja maior que 1 senão imprime igual
   print(' X ' if fato > 1 else ' = ',end='')
   rial *= fato
   fato -= 1
   resultado = rial
print(f'{resultado}')
#transformando o resultado em string
res = str(resultado)
res1 = res[0]
res2 = res[1]
#convertendo-os novamente a números inteiros
final = int(res1) + int(res2)
#apresentando o resultado final
print(f'E a soma dos digitos de n é {res1} + {res2} = {final}')
