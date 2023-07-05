num = int(input('Digite um número inteiro: '))
esc = int(input('''Escolha a base de conversão
1-Binário
2-Octal
3-Hexadecimal
'''))
if esc == 1:
    print(f'O número em binário é {bin(num)}')
elif esc == 2:
    print(f'O número em Octal é {oct(num)}')
elif esc == 3:
    print(f'O número em Hexadecimal é {hex(num)}')