from cpu import Cpu
from controladorInterrupcoes import ControladorInterrupcoes
from timer import Timer
from job import Job
#from escalonador import Escalonador

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
    #self._job3 = Job(open('./programas/prog1.txt', 'r'), self._timer.tempo_atual())
    #self._job4 = Job(open('./programas/prog2.txt', 'r'), self._timer.tempo_atual())

    self._lista_jobs.extend([self._job1, self._job2])#,self._job3, self._job4])

    self._job_atual = 0

    #inicia Cpu
    self._cpu = Cpu()
    self._carregar_programa()

    #inicia e roda o controlador
    self._controlador = ControladorInterrupcoes()
    self._controlador.execucao_cpu(self._cpu, self, self._timer)
  
  

  def __para(self):
    self._lista_jobs[self._job_atual].setFinalizado()
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
      if self._cpu.interrupcao() != 'PARA':    
        self._salva_cpu()    
        self._cpu.estado_dormencia()
        self._lista_jobs[self._job_atual].setDomir()
        self._timer.interrupcao('aperiodica', 0, 2, self._job_atual)
      return self._instrucoes_dic[instrucao]()
    else:
      print(f'INSTRUCAO ILEGAL! = {instrucao}')
      return self._instrucoes_dic["PARA"]()

  def resolve_interrupcao(self, codigo):
    #pedente , dormindo , finalizado
    self._lista_jobs[codigo].setPendente()
    self._lista_jobs[codigo].setPc(self._lista_jobs[codigo].getPc())
      
  def _salva_cpu(self):
    self._lista_jobs[self._job_atual].setPc(self._cpu.getPc())  
    self._lista_jobs[self._job_atual].setAcumulador(self._cpu.getAcumulador()) 
    self._lista_jobs[self._job_atual].setMem_dados(self._cpu.getMem_dados())

  def _checkar_pendencia(self):
    for i, job in enumerate(self._lista_jobs, start=0):
      if job.getStatus() == 'pendente': 
        return i
    return -1
  
  def _checkar_dormindo(self):
    for i, job in enumerate(self._lista_jobs, start=0):
      if job.getStatus() == 'dormindo': 
        return i
    return -1

  def _carregar_programa(self):
    self._job_atual = self._checkar_pendencia()
    if self._job_atual  != -1:
      self._cpu.altera_estado()
      self._cpu.altera_programa(self._lista_jobs[self._job_atual].getMem_prog())
      self._cpu.setMem_dados(self._lista_jobs[self._job_atual].getMem_dados())
      self._cpu.set_pc(self._lista_jobs[self._job_atual].getPc())