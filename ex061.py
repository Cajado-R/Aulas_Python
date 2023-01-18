#progressão  melhorada
num = int(input('Digite um número'))
razao = int(input('Digite o valor da razão: '))
vezes = 10
res = int
#enquanto o número de vezes que inicialmente era 10 for maior que 0:
while vezes > 0:
    #faça com que ele reduza em 1 a cada rodada
    vezes -= 1
    #e faça que o núemro seja somado a razão a cada vez
    num += razao
    #por fim printe o número
    print(num)

