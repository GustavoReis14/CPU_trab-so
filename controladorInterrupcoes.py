from cpu import Cpu

class ControladorInterrupcoes:
  

  def execucao_cpu(self, cpu, so, timer):
    comando = ''
    while cpu.interrupcao() == 'normal' or cpu.interrupcao() == 'dormindo' :


      timer.incrementa()

      print(f'TIMER : {timer.tempo_atual()}')
      print(f'JOB STATUS : {so._lista_jobs[0].getStatus()}')
      print(f'JOB STATUS : {so._lista_jobs[1].getStatus()}')
      print(f'JOB STATUS : {so._lista_jobs[2].getStatus()}')


      while True:
        cod_interrupcao = timer.pendencia()
        if cod_interrupcao == -1: break
        so.resolve_interrupcao(cod_interrupcao)
      
      if cpu.interrupcao() == 'normal':

        #executa programa
        cpu.executa()
        if cpu.interrupcao() != 'normal':
          revolvido = so.resolve_instrucao(cpu.instrucao())
          if so._lista_jobs[so._job_atual].getStatus() == 'finalizado' or so._lista_jobs[so._job_atual].getStatus() == 'dormindo':
            so._carregar_programa()
          if so._checkar_pendencia() == -1 and so._checkar_dormindo() == -1:
            break

        
      print('---------------')
      
          
        
      

