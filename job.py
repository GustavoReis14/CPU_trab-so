class Job:
  def __init__(self, programa, entrada_saida):
    self.__pc = 0
    self.__ax = 0
    self._programa = programa
    self._mem_dados = []
    self._status = 'pendente'

  def getPrograma(self):
    return self._programa

  def getMem_dados(self):
    return self._mem_dados
  
  def getStatus(self):
    return self._status

  def getAcumulador(self):
    return self.__ax

  def getPc(self):
    return self.__pc
    
  def setPc(self, pc):
    self.__pc = pc
  
  def setAcumulador(self, ax):
    self.__ax = ax
  
  def setMem_dados(self, mem):
    self._mem_dados = mem
    
  def status(self):
    print(f'PC = {self.__pc}\nAX = {self.__ax}\nMEM = {self._mem_dados}')

  def setFinalizado(self):
    self._status = 'finalizado'