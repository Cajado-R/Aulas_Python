num = n = s = 0
while n < 999:
    n = int(input("Digite um número de 1 a 998 se quiser parar digite 999"))
    num += 1
    if n >= 999 or n <= 0:
        num -= 1
        break
    s += n
    #F strings do python 3 (aprendido a partir dessa aula.)
print(f'vc digitou: {num} digitos antes de escolher parar digitando 999')
print(f'A soma é {s}')