preco = 121.50
print('METILFENIDATO: R$121.50')
formapag = int(input('1 - á vista din/cheque (10% de desconto)\n2 - á vista cartão (5% de desconto)\n3 - até 2x no cartão (valor cheio)\n4 - 3x ou mais (20% de juros)\n '))
if formapag == 1:
    print('Você irá pagar Á VISTA R${:.2f}'.format((preco - (10/100 * preco))))
elif formapag == 2:
    print('Você irá pagar Á VISTA no cartão R${:.2f}'.format((preco - (5 / 100 * preco))))
elif formapag == 3:
    print('Você irá pagar no cartão em até 2x R${:.2f} e pagara parcelas de R${}'.format(preco, preco/2))
elif formapag == 4:
    print('Você irá pagar no cartão em 3x ou mais {:.2f}'.format(preco + 20 / 100 * preco))
else:
    print('ERROR!')