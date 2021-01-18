from cpu import Cpu
from controladorInterrupcoes import ControladorInterrupcoes
from timer import Timer
from job import Job

class SistemaOperacional:
  def __init__(self):

    #instrucoes
    self._instrucoes_dic = {'PARA': self.__para, "LE": self.__le, "GRAVA": self.__grava}

    #timer
    self._timer = Timer()

    #Jobs
    self._lista_jobs = []
    self._job1 = Job(open('./programas/prog1.txt', 'r'), self._timer.tempo_atual())
    self._job2 = Job(open('./programas/prog2.txt', 'r'), self._timer.tempo_atual())

    self._lista_jobs.extend([self._job1, self._job2])

    self._job_atual = -1

    #inicia Cpu
    self._cpu = Cpu()

    for index, job in enumerate(self._lista_jobs, start=0):
      self._job_atual = index
      self._cpu.altera_estado()
      self._cpu.altera_programa(job.getPrograma())
      self._cpu.altera_dados()


    #inicia e roda o controlador
    self._controlador = ControladorInterrupcoes()
    self._controlador.execucao_cpu(self._cpu, self, self._timer)
    

  def __para(self):
    print("Exit")
    return False

  def __le(self):
    with open('0.txt', 'r') as conteudo:
      self._cpu.set_ax(int(conteudo.readline()))
    self._cpu.incrementa_pc()
    return True

  def __grava(self):
    with open('1.txt', 'w') as conteudo:
      conteudo.write(str(self._cpu.get_ax()))
    self._cpu.incrementa_pc()
    return True


  def resolve_instrucao(self, instrucao):
    if instrucao in self._instrucoes_dic:
      if instrucao != 'PARA':
        self._cpu.estado_dormencia()
        self._salvaCpu()

      return self._instrucoes_dic[instrucao]()
      
  def _salvaCpu(self):
    self._lista_jobs[self._job_atual].setPc(self._cpu.getPc())  
    self._lista_jobs[self._job_atual].setAcumulador(self._cpu.getAcumulador()) 
    self._lista_jobs[self._job_atual].setMem_dados(self._cpu.getMem_dados())
