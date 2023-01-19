contador = resultado =  0
numero = 1
while numero > 0:
    numero = int(input('Digite um número para obter a sua tabuada: '))
    print(50 * '-')
    while contador < 10 and numero > 0:
        contador += 1
        resultado = numero * contador
        print(f'{numero} X {contador} = {resultado}')
    if contador == 10:
        print(50 * '-')
        contador = 0
    if numero < 0:
        break
print('FIM DO PROGRAMA')


