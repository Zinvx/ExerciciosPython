prec = float(input('Digite o valor do produto: '))
forma = int(input('''Escolha o número da forma de pagamento:
1-À vista no dinheiro
2-À vista no cartão
3-2x no cartão
4-3x ou mais no cartão
'''))
if forma == 1:
    print(f'O valor será de R${prec-((10/100)*prec):.2f} com 10% de desconto')
elif forma == 2:
    print(f'O valor será de R${prec-((5/100)*prec):.2f} com 5% de desconto')
elif forma == 3:
    print(f'O valor será de R${prec:.2f}')
elif forma == 4:
    print(f'O valor será de R${prec+((20/100)*prec):.2f} com 20% de juros')