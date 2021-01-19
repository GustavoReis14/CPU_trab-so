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
          if not cod_interrupcao : break
          print(cod_interrupcao)
          so.resolve_interrupcao(cod_interrupcao)

        #executa programa
        print(f'JOB ATUAL {so._job_atual}')
        print(f'PC {cpu.getPc()}')
        print(f'MEM PROG {cpu.getMem_prog()}')
        print(f'MEM DADOS {cpu.getMem_dados()}')
        
        cpu.executa()
        print(f'ESTADO CPU {cpu.interrupcao()}')

        if cpu.interrupcao() != 'normal':
          print("ENTROU RESOLVE INSTRUCAO")
          revolvido = so.resolve_instrucao(cpu.instrucao())
          print(f'ESTADO CPU {cpu.interrupcao()}')
          print(f'STATUS {so._lista_jobs[so._job_atual].getStatus()}')
          if so._lista_jobs[so._job_atual].getStatus() == 'finalizado' or so._lista_jobs[so._job_atual].getStatus() == 'dormindo':
            so._carregar_programa()
          elif not so._checkar_pendencia() and not so._checkar_dormindo():
            break
          
          
        print('---------------------')


