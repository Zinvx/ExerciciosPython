maior = 0
menor = 0
for c in range(0,5):
   peso = float(input('Digite o peso: '))
   if (c == 1):
       maior = peso
       menor = peso
   else:
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print(f'O maior peso é {maior} e o menor é {menor}')