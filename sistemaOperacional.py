from cpu import Cpu
from controladorInterrupcoes import ControladorInterrupcoes

class SistemaOperacional:
  def __init__(self):
    self._file = open('inst.txt', 'r')
    
    #inicia Cpu
    self._cpu = Cpu()
    self._cpu.altera_estado()
    self._cpu.altera_programa(self._file)
    self._cpu.altera_dados()

    #inicia e roda o controlador
    self._controlador = ControladorInterrupcoes()
    self._controlador.execucao_cpu(self._cpu)


    self._resposta = 0
    print(f'CPU parou na instrucao {self._cpu.instrucao()}')
    print(f'O valor de m[{self._resposta}] eh {self._cpu.get_mem_dados_indice(self._resposta)}')