from cpu import Cpu
from controladorInterrupcoes import ControladorInterrupcoes

class SistemaOperacional:
  def __init__(self):
    self._file = open('inst.txt', 'r')

    #instrucoes
    self._instrucoes_dic = {'PARA': self.__para, "LE": self.__le, "GRAVA": self.__grava}

    #inicia Cpu
    self._cpu = Cpu()
    self._cpu.altera_estado()
    self._cpu.altera_programa(self._file)
    self._cpu.altera_dados()
    self._file.close()

    #inicia e roda o controlador
    self._controlador = ControladorInterrupcoes()
    self._controlador.execucao_cpu(self._cpu, self)


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
      return self._instrucoes_dic[instrucao]()
      