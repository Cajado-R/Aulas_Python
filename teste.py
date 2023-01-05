while True:
    print('1 - comeu')
    print('2 - não comeu')
    c = int(input('>'))
    if c == 1:
        print('Parabéns')
        break
    elif c == 2:
        print('Se alimente por favor')
        break
    else:
        continue
