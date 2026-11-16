import math
vetDad = []
dadosOrd = []
limitSup = []
limitInf = []
freqClass = []
freqAc = []
dados = (input("Digite os numeros inteiros : "))
vetDad = dados.split(" ")
for aux in vetDad:
    dadosOrd.append(int(aux))
print("Como gostaria de visualizar os dados informados ?")
informados = int(input(
    "Digite 1 para ver os dados Brutos\n Digite 2 para ver os dados da tabela de frequencia \n"))

if informados == 1:
    print("DADOS BRUTOS")
elif informados == 2:
    print("TABELA DE FREQUENCIA")
    dadosOrd = sorted(dadosOrd)
    A = dadosOrd[len(dadosOrd)-1]-dadosOrd[0]
    K = math.sqrt(len(dadosOrd))
    a = A/K
    intervalo = round(a)

    aux1 = dadosOrd[len(dadosOrd)-1]
    aux2 = dadosOrd[0]
    for var in range(aux1 + intervalo):
        if aux2 >= aux1 + intervalo:
            break
        else:
            limitInf.append(aux2)
            aux2 = aux2+intervalo
            limitSup.append(aux2)
    del (limitInf[len(limitInf)-1])
    del (limitSup[len(limitSup)-1])
    for inter in range(len(limitSup)):
        contador = 0
    for inter1 in range(len(dadosOrd)):
        if dadosOrd[inter1] >= limitInf[inter] and dadosOrd[inter1] <= limitSup[inter]:
            contador = contador+1
    freqClass.append(contador)

    # FreqAc
    inter = 0
    var1 = 0
    for inter in range(len(freqClass)):
        var1 = var1+freqClass[inter]
        freqAc.append(var1)

    # Media
    inter = 0
    auxMedia = []
    for inter in range(len(limitSup)):
        SomaMedia = ((limitInf[inter]+limitSup[inter])/2 * freqClass[inter])
        auxMedia.append(SomaMedia)
    Media = sum(auxMedia) / sum(freqClass)

    # Mediana
    Mediana = sum(freqClass)/2
    inter1 = 0
    for inter1 in range(len(limitSup)):
        if Mediana <= freqAc(inter1):
            limitInfMediana = limitInf(inter1)
            ResultMediana = limitInfMediana + \
                (((Mediana - freqAc[inter1 - 1])/freqClass[inter1*intervalo]))
            break

    # Moda
    inter3 = 0
    auxModa = []
    for inter3 in range(len(limitSup)):
        if freqClass(inter3) == max(freqClass):
            limitInfModa = limitInf(inter3)
        d1 = freqClass(inter3) - freqClass(inter3-1)
        d2 = freqClass(inter3) + freqClass(inter3+1)
        Moda = limitInfModa + (d1/(d1+d2)*intervalo)

    # Variancia
    auxVar = []
    ponto = 0
    var = 0
    for var in range(len(limitSup)):
        ponto = limitInf[var]+(intervalo/2)
        auxVar.append(math.pow(ponto - Media)*freqClass[var])
    Variancia = sum(auxVar)/(freqAc[len(freqAc)-1]-1)

    # Desvio Padrao
    DesvioPadrao = math.sqrt(Variancia)

    # Coeficiente Padrao
    CoeficierntePadrao = (DesvioPadrao/Media)*100

    # Quartis
    auxQuartis = []
    var = 0
    inter2 = 0
    for var in range(3):
        QTacumulado = (sum(freqClass[inter3])*(var+1))/4
        limitInfQuartis = limitInf[inter3]
        if inter2 == 0:
            quartis = limitInfQuartis + \
                (((QTacumulado-0)/freqClass[inter3])*inter)
        else:
            quartis = limitInfQuartis + \
                (((QTacumulado - freqAc[inter3-1]) /
                 freqClass[inter3])*intervalo)
        auxQuartis(round(quartis))
        break

    # Decis
    auxDecis = []
    var = 0
    inter2 = 0
    for var in range(3):
        DCacumulado = (sum(freqClass[inter3])*(var+1))/10
        limitInfDecis = limitInf[inter3]
        if DCacumulado <= freqAc[inter2]:
            Decis = limitInfDecis+(((DCacumulado-0)/freqClass[inter3])*inter)
        else:
            Decis = limitInfDecis + \
                (((DCacumulado - freqAc[inter3-1]) /
                 freqClass[inter3])*intervalo)
        auxDecis(round(quartis))
        break

    # Percentis
    auxPercent = []
    var = 0
    inter2 = 0
    for var in range(3):
        PCacumulado = (sum(freqClass[inter3])*(var+1))/10
        limitInfPercentil = limitInf[inter3]
        if PCacumulado <= freqAc[inter2]:
            Percentil = limitInfPercentil + \
                (((PCacumulado-0)/freqClass[inter3])*inter)
        else:
            Percentil = limitInfPercentil + \
                (((PCacumulado - freqAc[inter3-1]) /
                 freqClass[inter3])*intervalo)
        auxPercent(round(quartis))
        break

    print('Média : ', round(Media))
    print('- Mediana : ', round(Mediana))
    print('- Moda :', round(Moda))
    print('- Variancia : ', round(Variancia))
    print('- Desvio Padrão : ', round(DesvioPadrao))
    print('- Coeficiente de Variação : ', round(CoeficierntePadrao))
    print('- Qartil : ', auxQuartis)
    print('- Decil : ', auxDecis)
    print('- Percentil : ', auxPercent)
else:
    print('Valor inválido')
