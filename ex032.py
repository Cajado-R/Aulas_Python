anbi = int(input('Digite o ano para identificar se ele é bissexto: '))
if anbi % 4 == 0 and anbi % 100 != 0 or anbi % 400 == 0:
    print('Seu ano é bissexto')
else:
    print('Seu ano não é bissexto')