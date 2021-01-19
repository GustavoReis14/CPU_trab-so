class Cpu:
    def __init__(self):
      self.__pc = 0
      self.__ax = 0
      self.__estado = ''
      self.__motivo = ''
      self.__mem_prog = []
      self.__mem_prog_dic = {'CARGI': self.__cargi, 'CARGM': self.__cargm,
      'CARGX': self.__cargx, 'ARMM': self.__armm, 'ARMX': self.__armx,
      'SOMA': self.__soma, 'NEG': self.__neg, 'DESVZ': self.__desvz}
      self.__mem_dado = []



    def get_ax(self):
      return self.__ax

    def set_pc(self, v):
      self.__pc = v

    def set_ax(self, n):
      self.__ax = n

    def incrementa_pc(self):
      self.__pc += 1

    #coloca o valor n no acumulador (A=n)
    def __cargi(self, n):
      self.__ax = n
      self.__pc += 1

    #coloca no acumulador o valor na posição n da memória de dados (A=M[n])
    def __cargm(self, n):
      if (n >= len(self.__mem_dado)): 
        self.__estado = "violacao de memoria"
        self.__motivo = 'cargm '+ str(n)
      else :
        self.__ax = self.__mem_dado[n]
        self.__pc += 1
        
    #coloca no acumulador o valor na posição que está na posição n da memória de dados (A=M[M[n]])
    def __cargx(self, n):
      if (self.__mem_dado[n] >= len(self.__mem_dado)): 
        self.__estado = "violacao de memoria"
        self.__motivo = 'cargx '+ str(n)
      else :
        self.__ax = self.__mem_dado[self.__mem_dado[n]]
        self.__pc += 1

    #coloca o valor do acumulador na posição n da memória de dados (M[n]=A)
    def __armm(self, n):
      if (n >= len(self.__mem_dado)): 
        self.__estado = "violacao de memoria"
        self.__motivo = 'armm '+ str(n)
      else :
        self.__mem_dado[n] = self.__ax
        self.__pc += 1

    #coloca o valor do acumulador posição que está na posição n da memória de dados (M[M[n]]=A)
    def __armx(self, n):
      if (self.__mem_dado[n] >= len(self.__mem_dado)): 
        self.__estado = "violacao de memoria"
        self.__motivo = 'armx '+ str(n)
      else :
        self.__mem_dado[self.__mem_dado[n]] = self.__ax
        self.__pc += 1

    #soma ao acumulador o valor no endereço n da memória de dados (A=A+M[n])
    def __soma(self, n):
      if (n >= len(self.__mem_dado)): 
        self.__estado = "violacao de memoria"
        self.__motivo = 'soma '+ str(n)
      else :
        self.__ax += self.__mem_dado[n]
        self.__pc += 1

    #inverte o sinal do acumulador (A=-A)
    def __neg(self):
      self.__ax = self.__ax*-1
      self.__pc += 1

    #se A vale 0, coloca o valor n no __pc
    def __desvz(self, n):
      if (self.__ax == 0): 
        self.__pc = n
      else:
        self.__pc += 1
      if (n > len(self.__mem_dado)): 
        self.__estado = "violacao de memoria"
        self.__motivo = 'desvz '+ str(n)

    def altera_estado(self):
      self.__estado = 'normal'

    def altera_programa(self, prog):
      self.__mem_prog = prog

    def setMem_dados(self, v):
      self.__mem_dado = v
    
    def getMem_dados(self):
      return self.__mem_dado
    
    def interrupcao(self):    
      return self.__estado
    
    def retorna_interrupcao(self):
      if(self.__estado != 'normal'):
          self.__estado = 'normal'

    def instrucao(self):
      return self.__motivo
    
    def get_mem_dados_indice(self, indice):
      return self.__mem_dado[indice]

    def estado_dormencia(self):
      self.__estado = 'dormindo'
    
    def getMem_prog(self):
      return self.__mem_prog

    def getAcumulador(self):
      return self.__ax

    def getPc(self):
      return self.__pc
            

    def executa(self):
      comando = self.__mem_prog[self.__pc]
      if (len((self.__mem_prog[self.__pc]).split()) > 1): comando, valor = (self.__mem_prog[self.__pc]).split()
        

      if (comando == 'NEG'):
          self.__mem_prog_dic[comando]()
      elif comando in self.__mem_prog_dic:
          self.__mem_prog_dic[comando](int(valor))
      else:
          self.__estado = 'instrucao ilegal'
          self.__motivo = comando
          