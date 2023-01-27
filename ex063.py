print('Sequência de Fibonacci')
numeros = int(input('Digite quantos numeros da sequencia gostaria de ver? :'))
termo1 = 0
termo2 = 1
print(f'{termo1}→{termo2} ', end='→')
cont = 3
while cont <= numeros:
    termo3 = termo1 + termo2
    print(f'{termo3}', end='→')
    termo1 = termo2
    termo2 = termo3
    cont+=1

