from cpu import Cpu
from controladorInterrupcoes import ControladorInterrupcoes
from timer import Timer
from job import Job
from escalonador import Escalonador

class SistemaOperacional:
  def __init__(self):
    #instrucoes
    self.__instrucoes_dic = {'PARA': self.__para, "LE": self.__le, "GRAVA": self.__grava}

    #timer
    self.__timer = Timer()
    #aperiodica por enquanto
    self.__timer.criaInterrupcao('aperiodica',0, 10, 1000)

    #jobs / Escalonador
    self.__carregaJobs()

    #inicia Cpu
    self.__cpu = Cpu()

    #inicia e roda o controlador
    self.__controlador = ControladorInterrupcoes()
    self.__controlador.execucao_cpu(self.__cpu, self, self.__timer , self.__escalonador)
  
    print(f'JOB STATUS 1: {self.__escalonador.get_lista_jobs()[0].getStatus()}')
    print(f'JOB STATUS 2: {self.__escalonador.get_lista_jobs()[1].getStatus()}')
    print(f'JOB STATUS 3: {self.__escalonador.get_lista_jobs()[2].getStatus()}')
    print(f'JOB STATUS 4: {self.__escalonador.get_lista_jobs()[3].getStatus()}')

  def __carregaJobs(self):
    self.__lista_jobs = []
    self.__job1 = Job(open('./programas/prog1.txt', 'r'), self.__timer.getTempoAtual())
    self.__job2 = Job(open('./programas/prog1.txt', 'r'), self.__timer.getTempoAtual())
    self.__job3 = Job(open('./programas/prog2.txt', 'r'), self.__timer.getTempoAtual())
    self.__job4 = Job(open('./programas/prog2.txt', 'r'), self.__timer.getTempoAtual())

    self.__lista_jobs.extend([self.__job1, self.__job2, self.__job3, self.__job4])

    self.__escalonador = Escalonador(self.__lista_jobs)

  def __para(self, codigo):
    self.__escalonador.get_lista_jobs()[codigo].setStatusFinalizado()
    print("Exit - Programa Finalizado\n")
    return False
  
  def __le(self, codigo, valor):
    job = self.__escalonador.get_lista_jobs()[codigo]
    mem_prog = job.getMemProg()
    pc = job.getPc()
    instr = mem_prog[pc]
    acc = job.getAcumulador()
    with open(f'./entradas-saidas/0_{codigo}x{valor}.txt', 'r') as conteudo:
      job.setAcumulador(int(conteudo.readline()))
    self.__escalonador.get_lista_jobs()[codigo].incremantePc()
    print("RESOLVEU!!!! LE", codigo)
    if codigo == self.__escalonador.get_job_atual():
      self.__cpu.setAcumulador(job.getAcumulador())
      self.__cpu.setPc(job.getPc())
    return True
################################# LER LINHAS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
  def __grava(self, codigo, valor):
    job = self.__escalonador.get_lista_jobs()[codigo]
    mem_prog = job.getMemProg()
    pc = job.getPc()
    instr = mem_prog[pc]
    acc = job.getAcumulador()
    with open(f'./entradas-saidas/1_{codigo}x{valor}.txt', 'w') as conteudo:
      conteudo.write(str(acc))
    
    self.__escalonador.get_lista_jobs()[codigo].incremantePc()
    if codigo == self.__escalonador.get_job_atual():
      self.__cpu.setAcumulador(job.getAcumulador())
      self.__cpu.setPc(job.getPc())

    print("RESOLVEU!!!! GRAVA", codigo)

    return True

  def resolveInstrucaoIlegal(self, instrucao):
    print(f'INSTRUCAO ILEGAL! = {instrucao}')
    if instrucao in self.__instrucoes_dic:
      if instrucao != 'PARA':  
        self.__salvaCpu()    
        self.__cpu.setEstadoDormindo()
        self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].setStatusDormir()
        self.__timer.criaInterrupcao('aperiodica', 0, 2, self.__escalonador.get_job_atual())
        return self.__instrucoes_dic[instrucao]
      else:
        self.__cpu.setEstadoDormindo()
        return self.__instrucoes_dic["PARA"](self.__escalonador.get_job_atual())
    else:
      self.__escalonador.lista_jobs[self.__escalonador.job_atual].setStatusFinalizado()
      print("Instrução Ilegal\nExit - Programa Finalizado\n")

  def resolveInterrupcao(self, codigo):
    if codigo == 1000:
      print("inicializou o programa!!!!!!!!!!!")
      self.__escalonador.change_status()
      self.carregaPrograma()
    else:
      job = self.__escalonador.get_lista_jobs()[codigo]
      mem_prog = job.getMemProg()
      instrucao = mem_prog[job.getPc()]
      comando, valor = instrucao.split()
      self.__instrucoes_dic[comando](codigo, valor)
      
      if job.getStatus() != 'finalizado':
        job.setStatusPendente()
      self.__cpu.setEstadoNormal()
 
  def __salvaCpu(self):
    self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].setPc(self.__cpu.getPc())  
    self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].setAcumulador(self.__cpu.getAcumulador()) 
    self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].setMemDados(self.__cpu.getMemDados())

  def carregaPrograma(self):

    if self.__escalonador.checka_pendencia() != -1:
      self.__escalonador.set_job_atual(self.__escalonador.checka_pendencia(), self.__timer.getTempoAtual())
      self.__cpu.setEstadoNormal()
      self.__cpu.setMemPrograma(self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].getMemProg())
      self.__cpu.setMemDados(self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].getMemDados())
      self.__cpu.setPc(self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].getPc())
      self.__cpu.setAcumulador(self.__escalonador.get_lista_jobs()[self.__escalonador.get_job_atual()].getAcumulador())

if __name__ == '__main__':
  SistemaOperacional()