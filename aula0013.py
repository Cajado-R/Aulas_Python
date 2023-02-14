def mensagem(text):
    print('-' * 30)
    print(text)
    print('-' * 30)


mensagem('CURSO EM VÍDEO')
mensagem('APRENDA PYTHON')
mensagem('GUSTAVO GUANABARA')
mensagem(1)



def soma(a, b):
    s = a + b
    print(s)


soma(3, 6)
soma(2, 4)




def contando(* num):
    print(len(num))


contando(2, 3, 4, 7, 8)




def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [30, 201, 31, 21, 2121]
dobra(valores)
print(valores)






def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 3, 5)
soma(3, 13, 143032512512858165)