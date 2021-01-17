from cpu import Cpu

class ControladorInterrupcoes:
  

  def execucao_cpu(self, cpu):
    while cpu.interrupcao() == 'normal':
      cpu.executa()
    