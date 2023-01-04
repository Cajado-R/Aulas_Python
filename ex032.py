anbi = int(input('Digite o ano para identificar se ele é bissexto: '))
anbicalc = anbi % 4
if anbicalc == 0:
    print('Seu ano é bissexto')
else:
    print('Seu ano não é bissexto')