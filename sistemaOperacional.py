from cpu import Cpu
from controladorInterrupcoes import ControladorInterrupcoes
from timer import Timer
from job import Job
from escalonador import Escalonador

class SistemaOperacional:
  def __init__(self):
    #instrucoes
    self._instrucoes_dic = {'PARA': self.__para, "LE": self.__le, "GRAVA": self.__grava}

    #timer
    self._timer = Timer()
    #aperiodica por enquanto
    self._timer.interrupcao('aperiodica',0, 10, 1000)

    #jobs / Escalonador
    self.carregaJobs()

    #inicia Cpu
    self._cpu = Cpu()
    #self.carregar_programa()

    #inicia e roda o controlador
    self._controlador = ControladorInterrupcoes()
    self._controlador.execucao_cpu(self._cpu, self, self._timer , self.escalonador)
  
    print(f'JOB STATUS 1: {self.escalonador.get_lista_jobs()[0].getStatus()}')
    print(f'JOB STATUS 2: {self.escalonador.get_lista_jobs()[1].getStatus()}')
    print(f'JOB STATUS 3: {self.escalonador.get_lista_jobs()[2].getStatus()}')
    print(f'JOB STATUS 4: {self.escalonador.get_lista_jobs()[3].getStatus()}')

  def carregaJobs(self):
    self._lista_jobs = []
    self._job1 = Job(open('./programas/prog1.txt', 'r'), self._timer.tempo_atual())
    self._job2 = Job(open('./programas/prog2.txt', 'r'), self._timer.tempo_atual())
    self._job3 = Job(open('./programas/prog3.txt', 'r'), self._timer.tempo_atual())
    self._job4 = Job(open('./programas/prog2.txt', 'r'), self._timer.tempo_atual())

    self._lista_jobs.extend([self._job1, self._job2, self._job3, self._job4])

    self.escalonador = Escalonador(self._lista_jobs)

  def __para(self, codigo):
    self.escalonador.get_lista_jobs()[codigo].setFinalizado()
    print("Exit - Programa Finalizado\n")
    return False
  
  def __le(self, codigo):
    job = self.escalonador.get_lista_jobs()[codigo]
    mem_prog = job.getMem_prog()
    pc = job.getPc()
    instr = mem_prog[pc]
    acc = job.getAcumulador()
    with open('0.txt', 'r') as conteudo:
      job.setAcumulador(int(conteudo.readline()))
    self.escalonador.get_lista_jobs()[codigo].incrementa_pc()
    print("RESOLVEU!!!! LE", codigo)
    if codigo == self.escalonador.get_job_atual():
      self._cpu.set_ax(job.getAcumulador())
      self._cpu.set_pc(job.getPc())
    return True

  def __grava(self, codigo):
    job = self.escalonador.get_lista_jobs()[codigo]
    mem_prog = job.getMem_prog()
    pc = job.getPc()
    instr = mem_prog[pc]
    acc = job.getAcumulador()
    with open('1.txt', 'w') as conteudo:
      conteudo.write(str(acc))
    
    self.escalonador.get_lista_jobs()[codigo].incrementa_pc()
    if codigo == self.escalonador.get_job_atual():
      self._cpu.set_ax(job.getAcumulador())
      self._cpu.set_pc(job.getPc())

    print("RESOLVEU!!!! GRAVA", codigo)

    return True

  def resolve_instrucao(self, instrucao):
    print(f'INSTRUCAO ILEGAL! = {instrucao}')
    if instrucao in self._instrucoes_dic:
      if instrucao != 'PARA':  
        self._salva_cpu()    
        self._cpu.estado_dormencia()
        self.escalonador.get_lista_jobs()[self.escalonador.get_job_atual()].setDomir()
        self._timer.interrupcao('aperiodica', 0, 2, self.escalonador.get_job_atual())
        return self._instrucoes_dic[instrucao]
      else:
        self._cpu.estado_dormencia()
        return self._instrucoes_dic["PARA"](self.escalonador.get_job_atual())
    else:
      self.escalonador.lista_jobs[self.escalonador.job_atual].setFinalizado()
      print("Instrução Ilegal\nExit - Programa Finalizado\n")

  def resolve_interrupcao(self, codigo):
    if codigo == 1000:
      print("inicializou o programa!!!!!!!!!!!")
      #implementar leitura/gravacao de arquivo nos arquivos designados pelo parametro  
      self.escalonador.change_status()
      self.carregar_programa()
    else:
      job = self.escalonador.get_lista_jobs()[codigo]
      mem_prog = job.getMem_prog()
      instrucao = mem_prog[job.getPc()]
      comando, valor = instrucao.split()
      
      self._instrucoes_dic[comando](codigo)
      
      if job.getStatus() != 'finalizado':
        job.setPendente()
      self._cpu.altera_estado()
 
  def _salva_cpu(self):
    self.escalonador.get_lista_jobs()[self.escalonador.get_job_atual()].setPc(self._cpu.getPc())  
    self.escalonador.get_lista_jobs()[self.escalonador.get_job_atual()].setAcumulador(self._cpu.getAcumulador()) 
    self.escalonador.get_lista_jobs()[self.escalonador.get_job_atual()].setMem_dados(self._cpu.getMem_dados())

  def carregar_programa(self):

    if self.escalonador.checka_pendencia() != -1:
      self.escalonador.set_job_atual(self.escalonador.checka_pendencia(), self._timer.tempo_atual())
      self._cpu.altera_estado()
      self._cpu.altera_programa(self.escalonador.get_lista_jobs()[self.escalonador.get_job_atual()].getMem_prog())
      self._cpu.setMem_dados(self.escalonador.get_lista_jobs()[self.escalonador.get_job_atual()].getMem_dados())
      self._cpu.set_pc(self.escalonador.get_lista_jobs()[self.escalonador.get_job_atual()].getPc())

if __name__ == '__main__':
  SistemaOperacional()