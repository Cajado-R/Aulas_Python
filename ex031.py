kmnum = float(input('Digite o número de KM da sua viagem'))
if kmnum <= 200:
    print('Você terá que pagar R${:.2f} por {}Km'.format(kmnum * 0.50, kmnum))
else:
    print('A sua viagem ultrapassa 200Km e você irá pagar R${:.2f} por {}Km'.format(kmnum * 0.45, kmnum))
print('Tenha uma boa viagem!!')