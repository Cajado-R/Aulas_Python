lista = []
num5 = 5
while True:
    num = int(input('Digite um número: '))
    deseja_continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if deseja_continuar == 'S':
        lista.append(num)
        continue
    if deseja_continuar == 'N':
        lista.append(num)
        break
    else:
        print('[ERROR] APENAS "S/N" [ERROR]')
        lista.append(num)
        continue
print(50*'=-=')
if num5 in lista:
    print(f'O número {num5} está na lista!')
else:
    print(f'O número {num5} não está na lista!')
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista na forma inversa fica {lista}')
