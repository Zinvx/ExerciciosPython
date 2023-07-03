dis = float(input('Digite a distância da viagem em Km: '))
if dis>200:
    print(f'O valor da viagem é de R${dis*0.45:.2f}')
else:
    print(f'O valor da viagem é de R${dis*0.50:.2f}')