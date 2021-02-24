from cpu import Cpu

class ControladorInterrupcoes:
  

  def execucao_cpu(self, cpu, so, timer, escalonador):
    comando = ''
    while cpu.interrupcao() == 'normal' or cpu.interrupcao() == 'dormindo' :


      timer.incrementa()

      print(f'TIMER : {timer.tempo_atual()}')
      
      
      while True:
        cod_interrupcao = timer.pendencia()
        if cod_interrupcao == -1: break
        so.resolve_interrupcao(cod_interrupcao)
      
      if cpu.interrupcao() == 'normal' and escalonador.get_status() == True:

        #executa programa
        cpu.executa()
        if cpu.interrupcao() != 'normal':
          revolvido = so.resolve_instrucao(cpu.instrucao())
          if escalonador.get_lista_jobs()[escalonador.get_job_atual()].getStatus() == 'finalizado' or escalonador.get_lista_jobs()[escalonador.get_job_atual()].getStatus() == 'dormindo':
            so.carregar_programa()
          if escalonador.checka_pendencia() == -1 and escalonador.checka_dormindo() == -1:
            break

        
      print('---------------')
      
          
        
      

