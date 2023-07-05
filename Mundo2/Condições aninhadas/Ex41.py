ano = int(input('Digite o ano de nascimento: '))
idade = 2023-ano
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Júnior')
elif idade == 20:
    print('Sênior')
elif idade > 20:
    print('Master')