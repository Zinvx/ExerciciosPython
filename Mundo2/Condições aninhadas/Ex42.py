r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if (r1+r2) > r3 or (r1+r3) > r2 or (r2+r3) > r1:
    print('Forma um triângulo')
    if r1 == r2 == r3:
        print('Seu triângulo é equilátero')
    elif r1 != r2 != r3 != r1:
        print('Seu triângulo é Escaleno')
    else:
        print('Seu triângulo é isóseles')
else:
    print('Não forma um triângulo')
