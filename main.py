from cpu import Cpu

cpu = Cpu()

file = open('inst.txt', 'r')

cpu.executa(file)

cpu.altera_dados()
cpu.altera_programa()
cpu.interru__pcao()
