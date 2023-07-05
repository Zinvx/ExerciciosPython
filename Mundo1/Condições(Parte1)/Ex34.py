sal = float(input('Digite o valor do salário: '))
if sal <= 1250:
    print(f'O valor do salário será de {sal+((15/100)*sal):.2f}')
else:
    print(f'O valor do salário será de {sal+((10/100)*sal):.2f}')
1