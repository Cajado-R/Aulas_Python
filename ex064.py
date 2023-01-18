num = 0
n = 0
while n < 999:
    n = int(input("Digite um número de 1 a 998 se quiser parar digite 999"))
    num += 1
    if n >= 999:
        print('vc digitou: {} digitos antes de escolher parar digitando 999'.format(num))