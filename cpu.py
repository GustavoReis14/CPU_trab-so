class Cpu:
    def __init__(self):
       self.pc = 0
       self.ax = 0
       self.estado = "normal"
       self.mem_prog = {'CARGI': self.cargi, 'CARGM': self.cargm,
        'CARGX': self.cargx, 'ARMM': self.armm, 'ARMX': self.armx,
        'SOMA': self.soma, 'NEG': self.neg, 'DESVZ': self.desvz}
       self.mem_dado = [0 for x in range(10)]

    #coloca o valor n no acumulador (A=n)
    def cargi(self, n):
        self.ax = n
        print('Valor de AX' , self.ax)

    #coloca no acumulador o valor na posição n da memória de dados (A=M[n])
    def cargm(self, n):
        self.ax = self.mem_dado[n]
        print('Valor de AX', self.ax)
        
    #coloca no acumulador o valor na posição que está na posição n da memória de dados (A=M[M[n]])
    def cargx(self, n):
        self.ax = self.mem_dado[self.mem_dado[n]]
        print('Valor de AX', self.ax)

    #coloca o valor do acumulador na posição n da memória de dados (M[n]=A)
    def armm(self, n):
        self.mem_dado[n] = self.ax
        print('Valor de mem dado na pos ',n,  self.mem_dado)

    #coloca o valor do acumulador posição que está na posição n da memória de dados (M[M[n]]=A)
    def armx(self, n):
        self.mem_dado[self.mem_dado[n]] = self.ax
        print('Valor de mem dado na pos ',n,  self.mem_dado)

    #soma ao acumulador o valor no endereço n da memória de dados (A=A+M[n])
    def soma(self, n):
        self.ax += self.mem_dado[n]
        print('Valor de AX', self.ax)

    #inverte o sinal do acumulador (A=-A)
    def neg(self):
        self.ax = self.ax*-1
        print('Valor de AX', self.ax)

    #se A vale 0, coloca o valor n no PC
    def desvz(self, n):
        if (self.ax == 0):
            self.pc = n

    def executa(self,comando, valor):
        if self.estado == "normal":
            if (comando == 'NEG'):
                self.mem_prog[comando]()
            elif comando in self.mem_prog:
                self.mem_prog[comando](valor)
            else:
                self.estado = "ilegal"
