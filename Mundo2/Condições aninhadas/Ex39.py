nasc = int(input('Digite seu ano de nascimento: '))
idade = 2023-nasc
if idade < 18:
    print(f'Você ainda irá se alistar daqui a {18-idade} anos')
elif idade == 18:
    print('Parabéns, chegou sua hora de se alistar')
elif idade > 18:
    print(f'Ou você já se alistou ou você passou {idade-18} anos do prazo')