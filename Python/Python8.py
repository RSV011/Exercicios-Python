notas=[]
notasInver=[]
acimaMedia=[]
abaixoDe7=[]
r=1
aux=0
soma=0
while r!=-1:
   r=int(input('Isnsira uma nota: '))
   notas.append(r)
   soma=soma+notas[aux]
   aux=aux+1
for i in range(0,len(notasInver)-1): 
        for j in range(len(notasInver)-1): 
            if(notasInver[j]<notasInver[j+1]): 
                temp=notasInver[j] 
                notasInver[j]=notasInver[j+1] 
                notasInver[j+1]=temp
media=soma/aux
for nota in notas:
    if nota>media:
        acimaMedia.append(nota)
for nota in notas:
    if nota>7:
        abaixoDe7.append(nota)
print(f'Quantidade de valores lidos: {aux}\nValores lidos: {notas}')
print('Notas invertidas')
for nota in notasInver:
    print(nota)
print(f'Soma dos valores: {soma}\nMedia dos valores: {media}\nValores acima da media: {acimaMedia}\nValores abaixo de 7: {abaixoDe7}')
print('Fim do Programa. ')