numeros=[]
impares=[]
pares=[]
aux=0
while aux<20:
    numero=int(input('Isnsira uma numero: '))
    numeros.append(numero)
    if (numero%2)!=0:
        impares.append(numero)
    elif (numero%2)==0:
        pares.append(numero)
    aux=aux+1
print(f'Numeros: {numeros}\nImpares: {impares}\nPares: {pares}')