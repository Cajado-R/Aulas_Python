"""num = int(input('Digite um número para receber o seu fatorial '))
ls = int
for c in range (num):
    ls = (num-1) * num
    print(num)"""
num = int(input('Digite um número para recebero fatorial: '))
fa = num
to = 1
print('{}'.format(num), end='')
while fa > 0:
   print('{}'.format(fa), end='')
   print(' X 'if fa > 1 else ' = ',end='')
   to *= fa
   fa -= 1
print('{}'.format(to))
