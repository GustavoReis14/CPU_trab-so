from cpu import Cpu

class ControladorInterrupcoes:
  

  def execucao_cpu(self, cpu, so, timer):
    comando = ''
    while cpu.interrupcao() == 'normal' or cpu.interrupcao() == 'dormindo' :
      
      if cpu.interrupcao() == 'normal':
        #lidando com interrupcao
        timer.incrementa()
        while True:
          cod_interrupcao = timer.pendencia()
          if(cod_interrupcao == -1): break
          so.resolve_interrupcao(cod_interrupcao)

        #executa programa
        cpu.executa()
        if cpu.interrupcao() != 'normal':
          revolvido = so.resolve_instrucao(cpu.instrucao())
          if revolvido:
            cpu.altera_estado()




    