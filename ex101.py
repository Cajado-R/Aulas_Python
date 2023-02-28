def voto():
    """
    Verifica se o contribuinte vota (vide leis do Brasil)
    :return: retorna a situação de voto.
    """
    import datetime
    data = datetime.date(2023, 2, 28)
    ano = data.year
    global idade, vt
    idade = ano - AnoDeNascimento

    if idade >= 18:
        if idade <= 65:
            vt = f"Com {idade} obrigatório"
            return vt
        elif 18 >= idade >= 16 or idade > 65:
            vt = f"Com {idade} opcional"
            return vt
    else:
        vt = f"Com {idade} não vota"
        return vt



AnoDeNascimento = int(input('Digite seu ano de nascimento [EX: 1900] '))
voto()
print(vt)


