class Escalonador:
  def __init__(self, lista_jobs):
    self.lista_jobs = lista_jobs
    self.job_atual = self.checka_pendencia()

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

  def set_job_atual(self, job):
    self.job_atual = job

  def get_job_atual(self):
    return self.job_atual

  def get_lista_jobs(self):
    return self.lista_jobs