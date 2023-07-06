s=0
num = int(input('Digite um número: '))
for c in range(2, num):
    if num%c == 0:
        s+=1
if s == 0:
    print('É primo')

