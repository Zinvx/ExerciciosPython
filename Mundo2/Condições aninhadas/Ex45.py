import time
from random import randint

selec = int(input('''Bem vindo ao jokenpô, selecione o número da sua jogada
1-Pedra
2-Papel
3-Tesoura
'''))
pc = randint(1,3)
print('Aguarde a máquina jogar')
time.sleep(2)
if pc == 1 and selec == 1:
    print(f'Empate, pc={pc}')
elif pc == 1 and selec == 2:
    print(f'Você ganhou, pc={pc}!')
elif pc == 1 and selec == 3:
    print(f'Você perdeu, pc={pc}')
elif pc == 2 and selec == 1:
    print(f'Você perdeu, pc={pc}')
elif pc == 2 and selec == 2:
    print(f'Empate, pc={pc}')
elif pc == 2 and selec == 3:
    print(f'Você ganhou, pc={pc}')
elif pc == 3 and selec == 1:
    print(f'Você ganhou, pc={pc}')
elif pc == 3 and selec == 2:
    print(f'Você perdeu, pc={pc}')
elif pc == 3 and selec == 3:
    print(f'Empate, pc={pc}')
