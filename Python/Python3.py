nota1=input('Insira a primeira nota: ')
nota2=input('Insira a segunda nota: ')
media=int(nota1)+int(nota2)/2
if media>=7 and media<10:
    print('Aprovado')
elif media<7:
    print('Reprovado')
elif media==10:
    print('Aprovado com Distinção')