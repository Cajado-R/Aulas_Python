numero = int(input('Digite um número para descobrir se é primo: '))
recebe = 0
for c in range (2, numero):
    if (numero % c == 0):
        recebe = 1
if(recebe == 0 and numero != 1):
    print('É primo')
else:
    print('Não é primo')