class Escalonador:
  def __init__(self, lista_jobs):
    self.lista_jobs = lista_jobs
    self.job_atual = self.checka_pendencia()
    self.status = False

  def checka_pendencia(self):
    for i, job in enumerate(self.lista_jobs, start=0):
      if job.getStatus() == 'pendente': 
        return i
    return -1
    
  def checka_dormindo(self):
    for i, job in enumerate(self.lista_jobs, start=0):
      if job.getStatus() == 'dormindo': 
        return i
    return -1

  def set_job_atual(self, job, timer):
    self.job_atual = job
    #Só altera o timer na primeira chamada do JOB
    if self.lista_jobs[self.job_atual].getTimer() == 0:
      self.lista_jobs[self.job_atual].setTimer(timer)
      print("TEMPO ATUAL",self.lista_jobs[self.job_atual].getTimer())
    else:
      print("JA INICIOU NO TEMPO", self.lista_jobs[self.job_atual].getTimer())

  def get_job_atual(self):
    return self.job_atual

  def get_lista_jobs(self):
    return self.lista_jobs

  def change_status(self):
    self.status = not self.status

  def get_status(self):
    return self.status