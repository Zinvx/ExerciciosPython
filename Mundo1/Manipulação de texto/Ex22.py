nome = input('Digite seu nome completo ')
lmai = nome.upper()
lmin = nome.lower()
lat = len(nome)-nome.count(' ')
pn = nome.split()
ql = len(pn[0])
print(f'''{lmai}
{lmin}
{lat} Letras
{ql} Letras''')
