frase = str(input('Digite uma frase: ')).lower()
frase = ''.join(frase.split())
frase2 = frase[::-1]
if frase2 == frase:
    print('É palíndromo')