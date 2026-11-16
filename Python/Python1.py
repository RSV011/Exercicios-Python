tamanhoArea=input('Insira o tamanho da área a ser pintada em metros quadrados: ')
litros=float(tamanhoArea)/3
latas=litros/18
sobra=litros%18
while sobra>0:
    sobra-18
    latas+1
preco=latas*80,00
print(f'serão necessárias {latas} latas. \nO preço total será de {preco}')