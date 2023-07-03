vel = float(input('Digite a velocidade do carro em Km: '))
if vel > 80:
    multa = (vel-80)*7
else:
    print('Você não foi multado')
if vel > 80:
    print(f'Você foi multado, sua multa equivale a R${multa:.2f}')