frase = input('Digite uma frase: ').lower()
Qv = frase.count('a')
Pv = frase.find('a')
Uv = frase.rfind('a')
print(f'''A letra 'a' se repete {Qv}
O primeiro 'a' é {Pv} 
O último 'a' é {Uv}''')