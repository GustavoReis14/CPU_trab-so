class Cpu:
    def __init__(self):
      self.__pc = 0
      self.__ax = 0
      self.__estado = 'normal'
      self.__comando_ilegal = ''
      self.__mem_prog = []
      self.__mem_prog_dic = {'CARGI': self.__cargi, 'CARGM': self.__cargm,
      'CARGX': self.__cargx, 'ARMM': self.__armm, 'ARMX': self.__armx,
      'SOMA': self.__soma, 'NEG': self.__neg, 'DESVZ': self.__desvz}
      self.__mem_dado = []
      self.__comando_atual = ''

    #coloca o valor n no acumulador (A=n)
    def __cargi(self, n):
      self.setAcumulador(n)
      self.incrementaPc()

    #coloca no acumulador o valor na posição n da memória de dados (A=M[n])
    def __cargm(self, n):
      if (n >= len(self.getMemDados())): 
        self.setEstadoViolacaoMem()
        self.__comando_ilegal = 'cargm '+ str(n)
      else :
        self.setAcumulador(self.getMemDadosNoIndice(n))
        self.incrementaPc()
        
    #coloca no acumulador o valor na posição que está na posição n da memória de dados (A=M[M[n]])
    def __cargx(self, n):
      if (self.getMemDadosNoIndice(n) >= len(self.__mem_dado)): 
        self.setEstadoViolacaoMem()
        self.__comando_ilegal = 'cargx '+ str(n)
      else :
        self.setAcumulador(self.__mem_dado[self.getMemDadosNoIndice(n)])
        self.incrementaPc()

    #coloca o valor do acumulador na posição n da memória de dados (M[n]=A)
    def __armm(self, n):
      if (n >= len(self.__mem_dado)): 
        self.setEstadoViolacaoMem()
        self.__comando_ilegal = 'armm '+ str(n)
      else :
        self.__mem_dado[n] = self.__ax
        self.incrementaPc()

    #coloca o valor do acumulador posição que está na posição n da memória de dados (M[M[n]]=A)
    def __armx(self, n):
      if (self.getMemDadosNoIndice(n) >= len(self.__mem_dado)): 
        self.setEstadoViolacaoMem()
        self.__comando_ilegal = 'armx '+ str(n)
      else :
        self.__mem_dado[self.getMemDadosNoIndice(n)] = self.__ax
        self.incrementaPc()

    #soma ao acumulador o valor no endereço n da memória de dados (A=A+M[n])
    def __soma(self, n):
      if (n >= len(self.__mem_dado)): 
        self.setEstadoViolacaoMem()
        self.__comando_ilegal = 'soma '+ str(n)
      else :
        self.__ax += self.getMemDadosNoIndice(n)
        self.incrementaPc()

    #inverte o sinal do acumulador (A=-A)
    def __neg(self):
      self.setAcumulador(self.__ax*-1)
      self.incrementaPc()

    #se A vale 0, coloca o valor n no __pc
    def __desvz(self, n):
      if (self.__ax == 0): 
        self.setPc(n)
      else:
        self.incrementaPc()
      if (n > len(self.__mem_dado)): 
        self.setEstadoViolacaoMem()
        self.__comando_ilegal = 'desvz '+ str(n)

    def getEstado(self):    
      return self.__estado

    def setEstadoNormal(self):
      self.__estado = 'normal'

    def setEstadoDormindo(self):
      self.__estado = 'dormindo'

    def setEstadoViolacaoMem(self):
      self.__estado = "violacao de memoria"

    def getMemPrograma(self):
      return self.__mem_prog

    def setMemPrograma(self, prog):
      self.__mem_prog = prog
    
    def getMemDados(self):
      return self.__mem_dado
    
    def setMemDados(self, v):
      self.__mem_dado = v
    
    def getMemDadosNoIndice(self, indice):
      return self.__mem_dado[indice]
    
    def setMemDadosNoIndice(self, indice, v):
        self.__mem_dado[indice] = v

    def getComandoIlegal(self):
      return self.__comando_ilegal

    def getAcumulador(self):
      return self.__ax

    def setAcumulador(self, n):
      self.__ax = n

    def getPc(self):
      return self.__pc

    def setPc(self, v):
      self.__pc = v

    def incrementaPc(self):
      self.setPc(self.getPc() + 1)

    def executa(self):
      comando = self.__mem_prog[self.__pc]
      if (len((self.__mem_prog[self.__pc]).split()) > 1): comando, valor = (self.__mem_prog[self.__pc]).split()
      self.__comando_atual = comando

      if (comando == 'NEG'):
          self.__mem_prog_dic[comando]()
      elif comando in self.__mem_prog_dic:
          self.__mem_prog_dic[comando](int(valor))
      else:
          self.__estado = 'instrucao ilegal'
          self.__comando_ilegal = comando
          