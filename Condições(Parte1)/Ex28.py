from random import randint
num = randint(1,5)
resp = int(input('Digite a resposta: '))
if resp == num:
    print('Parabéns, você acertou!')
else:
    print(f'Você errou, a resposta era {num}')