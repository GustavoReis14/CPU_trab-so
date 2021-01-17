from cpu import Cpu

class ControladorInterrupcoes:
  

  def execucao_cpu(self, cpu, so):
    comando = ''
    while cpu.interrupcao() == 'normal':
      cpu.executa()
      if cpu.interrupcao() != 'normal':
        revolvido = so.resolve_instrucao(cpu.instrucao())
        if revolvido:
          cpu.altera_estado()




    