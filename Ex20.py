from random import sample
aluno1 = input('Digite o primeiro nome: ')
aluno2 = input('Digite o segundo nome ')
aluno3 = input('Digite o terceiro nome ')
aluno4 = input('Digite o quarto nome ')
print(f'A ordem de apresentações será {sample([aluno1, aluno2, aluno3, aluno4], counts=[1,1,1,1], k=4) }')