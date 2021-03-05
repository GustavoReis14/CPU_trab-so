class Job:
  def __init__(self, programa, timer):
    self.__pc = 0
    self.__ax = 0
    self.__mem_prog = [line.replace('\n','').upper() for line in programa]
    self.__mem_dados = [0 for _ in range(20)]
    self.__status = 'pendente'
    self.__timer = timer
    self.__prioridade = 0.5
    

  def getMemProg(self):
    return self.__mem_prog

  def getMemDados(self):
    return self.__mem_dados
  
  def getPc(self):
    return self.__pc
    
  def setPc(self, pc):
    self.__pc = pc

  def incremantePc(self):
    self.__pc += 1

  def getStatus(self):
    return self.__status
  
  def setStatusPendente(self):
    self.__status = 'pendente'

  def setStatusFinalizado(self):
    self.__status = 'finalizado'

  def setStatusDormir(self):
    self.__status = 'dormindo'

  def getAcumulador(self):
    return self.__ax

  def setAcumulador(self, v):
    self.__ax = v
  
  def setMemDados(self, mem):
    self.__mem_dados = mem

  def getTimer(self):
    return self.__timer

  def setTimer(self, timer):
    self.__timer = timer

  def getPrioridade(self):
    return self.__prioridade

  def setPrioridade(self, prio):
    self.__prioridade = prio