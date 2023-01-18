# progressão  melhorada          #REFAZER!!!
num = int(input('Digite um número'))
razao = int(input('Digite o valor da razão: '))
vezes = 10
responda = 2
# enquanto o número de vezes que inicialmente era 10 for maior que 0:
while vezes > 0:
    # faça com que ele reduza em 1 a cada rodada
    vezes -= 1
    # e faça que o núemro seja somado a razão a cada vez
    num += razao
    # por fim printe o número
    print(num)
    while vezes == 0 and responda > 0:
        responda = int(input('Quer continuar mais quantas vezes? '))
        if responda != 0:
                    vezes = responda
                    vezes -= 1
                    num += razao
                    print(num)
        elif responda == 0:
            print('FIM')




