nome = input('Digite seu nome completo: ').split()
rev = nome[::-1]
print(f'''Seu primeiro nome é {nome[0]}.
Seu último nome é {rev[0]}.Z''')