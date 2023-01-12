n = int(input('Digite um número para saber sua tabuada: '))
for c in range(-1, 10):
    print('{:.0f} X {:.0f} = {:.0f}'.format(c+1, n, n*(c+1)))
