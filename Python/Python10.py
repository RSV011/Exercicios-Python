class CPF:
    def TesteDeCPF(self,CPF1):
        Resto = 0
        Soma = 0
        if CPF1 == "00000000000":
            return False
        for n in range (1,10):
          Soma = Soma + int(CPF1[n-1:n]) * (11 - n)
        Resto = (Soma * 10) % 11

        if Resto == 10 or Resto == 11:
            Resto = 0
        if Resto != int(CPF1[9:10]):
            return False

        Soma = 0
        for n in range (1,11):
            Soma = Soma + int(CPF1[n-1:n]) * (12 - n)
        Resto = (Soma * 10) % 11

        if Resto == 10 or Resto == 11:
            Resto = 0;
        if Resto != int(CPF1[10:11]):
            return False
        return True
m = CPF()
CPF1 = "12345678909"
CPF1 = input('Informe seu CPF: ')
print(m.TesteDeCPF(CPF1))