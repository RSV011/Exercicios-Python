tamanho=input('Insira o tamanho do arquivo em MB: ')
velocidade=input('Insira a velocidade do link de internet em Mbps: ')
seg=float(tamanho)/float(velocidade)
min=seg/60
print(f'Serão necessarios: {int(min)}:{int(seg)} min')