s=input('Insira o salario a ser reajustado: ')
salario=float(s)
if salario<280.00:
    aumento=(salario*20)/100
    novoSal=salario+aumento
    print(f'Salário antes do reajuste: {salario}\nPercentual de aumento aplicado: 20%\nValor do aumento: {aumento}\nNovo salário: {novoSal}')
elif salario>=280.00 and salario<700:
    aumento=(salario*15)/100
    novoSal=salario+aumento
    print(f'Salário antes do reajuste: {salario}\nPercentual de aumento aplicado: 15%\nValor do aumento: {aumento}\nNovo salário: {novoSal}')
elif salario>=700.00 and salario<1500:
    aumento=(salario*10)/100
    novoSal=salario+aumento
    print(f'Salário antes do reajuste: {salario}\nPercentual de aumento aplicado: 10%\nValor do aumento: {aumento}\nNovo salário: {novoSal}')  
elif salario>1500:
    aumento=(salario*5)/100
    novoSal=salario+aumento
    print(f'Salário antes do reajuste: {salario}\nPercentual de aumento aplicado: 5%\nValor do aumento: {aumento}\nNovo salário: {novoSal}')  