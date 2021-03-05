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
      

      print(f'JOB ATUAL : {escalonador.get_job_atual() if escalonador.get_status() else "None"}')
      if cpu.getEstado() == 'normal' and escalonador.get_status() == True:
      
        #executa programa
        cpu.executa()
        if cpu.getEstado() != 'normal':
          resolvido = so.resolveInstrucaoIlegal(cpu.getComandoIlegal())

          if escalonador.get_lista_jobs()[escalonador.get_job_atual()].getStatus() == 'finalizado' or escalonador.get_lista_jobs()[escalonador.get_job_atual()].getStatus() == 'dormindo':
            so.carregaPrograma()
          if escalonador.checka_pendencia() == -1 and escalonador.checka_dormindo() == -1:
            break

        
      print('---------------')
      
          
        
      

