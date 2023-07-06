idades = 0
velho = 0
nomevelho = 0
quantM = 0
for c in range(1,5):
    nome = str(input(f'Digite um nome: '.format(c))).capitalize()
    idade = int(input(f'Digite sua idade: '.format(c)))
    sexo = str(input(f'Opção sexual: '.format(c))).upper()
    print('_'*30)
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nomevelho = nome
    if sexo == 'F':
        if idade < 20:
            quantM += 1
    idades += idade
print('A media das idades do grupo é {}, no grupo tem {} mulher(es) abaixo dos 20 e {} é homem mais velho.'.format((idades/4),quantM,nomevelho))