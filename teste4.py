n = int(input('Digite quantos numeros da sequencia gostaria de ver? ; '))
c = 0
f = 0
if c == 0:
    print(f)
    c = 1
    f2 = 1
    print(f2)
    while c < (n - 1):
        x = f + f2
        print(x)
        c += 1
        f = f2
        f2 = x
print('')
print(f'Sequência finalizada com {n} termos.')