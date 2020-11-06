from cpu import Cpu

file = open('inst.txt', 'r')

cpu = Cpu()

cpu.altera_estado()
cpu.altera_programa(file)
cpu.altera_dados()

while cpu.interrupcao() == 'normal':
    cpu.executa()


resposta = 2
print(f'CPU parou na instrucao {cpu.instrucao()}')
print(f'O valor de m[{resposta}] eh {cpu.get_mem_dados_indice(resposta)}')
