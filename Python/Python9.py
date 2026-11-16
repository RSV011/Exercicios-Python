notas=[]
notasInver=[]
acimaDaMedia=[]
abaixoDe7=[]
r=1
s=1
aux=0
soma=0
while r!=-1:
   r=int(input('Isnsira uma nota(digite -1 para parar): '))
   notas.append(r)
   soma=soma+notas[aux]
   aux=aux+1
   media=soma/aux
def InformaValores(notas):
    return notas
def QuantidadeValores():
    return aux
def SomaValores():
    return soma
def MediaValores():
    return media
def AcimaMedia(notas):
    for nota in notas:
        if nota>media:
            acimaDaMedia.append(nota)
    return acimaDaMedia
def Abaixo7(notas):
    for nota in notas:
        if nota>7:
            abaixoDe7.append(nota)
    return abaixoDe7
def NotaInvertida(notasInver):
    for i in range(0,len(notasInver)-1): 
        for j in range(len(notasInver)-1): 
            if(notasInver[j]<notasInver[j+1]): 
                temp=notasInver[j] 
                notasInver[j]=notasInver[j+1] 
                notasInver[j+1]=temp
    for nota in notasInver:
        return nota
def Encerrar():
    print('Fim do Programa. ')
while s!=-1:
    s= int(input('Digite: \n1. Para mostrar a quantidade de notas.\n2. Para exibir as notas.\n3. Para exibir as notas em ordem inversa.\n4. Para exibir a soma das notas.\n5. Para exibir a média das notas.\n6. Para exibir a quantidades de notas acima da média.\n7. Para exibir a quantidade de notas abaixo de 7.\n-1. Para encerrar.'))
    if s==1:
        print(f'Quantidade de notas: {QuantidadeValores()}')
    elif s==2:
        print(f'Notas: {InformaValores(notas)}')
    elif s==3:
        print(f'Notas em ordem inversa: \n{NotaInvertida(notasInver)}')
    elif s==4:
        print(f'Soma das notas: {SomaValores()}')
    elif s==5:
        print(f'Media das notas: {MediaValores()}')
    elif s==6:
        print(f'Notas acima da media: {AcimaMedia()}')
    elif s==7:
        print(f'Valores abaixo de sete: {Abaixo7()}')
Encerrar()