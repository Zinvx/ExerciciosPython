ano = int(input('Digite o ano: '))
if ano%4 == 0:
   if ano%100 != 0:
       print('Não é bissexto')
   else:
       print('É bissexto')
else:
    if ano%400 == 0:
        print('É bissexto')
    else:
        print('Não é bissexto')
