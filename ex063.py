print('Sequência de Fibonacci')
numeros = int(input('Digite quantos numeros da sequencia gostaria de ver? :'))
comeco = 0
fibonacci = 0
if comeco == 1:
    comeco = 1
    fibonacci2 = 1
    while comeco < (numeros - 1):
        x = fibonacci + fibonacci2
        print(x, end='>>>')
        comeco += 1
        fibonacci = fibonacci2
        fibonacci2 = x
print(f'\nSua sequência foi finalizada!')