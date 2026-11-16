idades=[]
r='s'
aux=0
soma=0
while r=='s':
   idades.append(int(input('Isnsira uma idade: ')))
   r=input('Continuar? [S/N]')
   soma=soma+idades[aux]
   aux=aux+1
media=soma/aux
if media>=0 and media<=25:
    print('A turma jovem. ')
elif media>=26 and media<=60:
    print('A turma adulta. ')
elif media>60:
    print('A turma idosa. ')
