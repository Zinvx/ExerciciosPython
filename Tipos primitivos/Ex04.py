val = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(val))
print('Só tem espaços? ', val.isspace())
print('É um número? ', val.isnumeric())
print('É alfabético? ', val.isalpha())
print('É alfanumérico? ', val.isalnum())
print('Está em maiúsculas? ', val.isupper())
print('Está em minúsculas? ', val.islower())
print('É capítalizado? ', val.istitle())


