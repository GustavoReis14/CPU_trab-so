from cpu import Cpu

class ControladorInterrupcoes:
  

  def execucao_cpu(self, cpu, so, timer, escalonador):
    comando = ''
    while cpu.getEstado() == 'normal' or cpu.getEstado() == 'dormindo' :


      timer.incrementa()

      print(f'TIMER : {timer.getTempoAtual()}')
      
      
      while True:
        cod_interrupcao = timer.cheackInterrupcaoPendente()
        if cod_interrupcao == -1: break
        so.resolveInterrupcao(cod_interrupcao)
      

      print(f'JOB ATUAL : {escalonador.getJobAtualIndex() if escalonador.getStatus() else "None"}')
      if cpu.getEstado() == 'normal' and escalonador.getStatus() == True:
      
        #executa programa
        cpu.executa()
        if cpu.getEstado() != 'normal':
          resolvido = so.resolveInstrucaoIlegal(cpu.getComandoIlegal())

          if escalonador.getJobAtual().getStatus() == 'finalizado' or escalonador.getJobAtual().getStatus() == 'dormindo':
            so.carregaPrograma()
          if escalonador.checkaJobPendente() == -1 and escalonador.checkaJobDormindo() == -1:
            break

        
      print('---------------')
      
          
        
      

