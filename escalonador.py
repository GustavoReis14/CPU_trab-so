class Escalonador:
  def __init__(self, lista_jobs):
    self.__lista_jobs = lista_jobs
    self.__job_atual = self.checkaJobPendente()
    self.__status = False

  def checkaJobPendente(self):
    for i, job in enumerate(self.__lista_jobs, start=0):
      if job.getStatus() == 'pendente': 
        return i
    return -1
    
  def checkaJobDormindo(self):
    for i, job in enumerate(self.__lista_jobs, start=0):
      if job.getStatus() == 'dormindo': 
        return i
    return -1

  def getJobAtualIndex(self):
    return self.__job_atual
     
  def setJobAtual(self, job, timer):
    self.__job_atual = job
    #Só altera o timer na primeira chamada do JOB
    if self.__lista_jobs[self.__job_atual].getTimer() == 0:
      self.__lista_jobs[self.__job_atual].setTimer(timer)
      print("TEMPO ATUAL",self.__lista_jobs[self.__job_atual].getTimer())
    else:
      print("JA INICIOU NO TEMPO", self.__lista_jobs[self.__job_atual].getTimer())

  def getListaJobs(self):
    return self.__lista_jobs

  def alteraStatus(self):
    self.__status = not self.__status

  def getStatus(self):

    return self.__status

  def getJobAtual(self):
    return self.getListaJobs()[self.getJobAtualIndex()]