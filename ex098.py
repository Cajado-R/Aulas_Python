def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont,end=' ')
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(cont,end=' ')
            cont -= passo




contador(0, 10, 1)
print()
contador(10, 0, 1)
in1 = int(input('\nInicio: \n'))
fi = int(input('Fim: \n'))
pas = int(input('Passo: \n'))
contador(in1, fi, pas)

