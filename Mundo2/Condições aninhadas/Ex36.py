val = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do salário: '))
ano = int(input('Digite em quantos anos: '))
porc = sal*0.3
meses = ano*12
prest = val/meses
if prest <= porc:
    print('Seu emprestimo foi aprovado!')
elif prest > porc:
    print('Seu empréstimo foi negado')