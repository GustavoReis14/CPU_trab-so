from cpu import Cpu

cpu = Cpu()

while True:
    
    comando = input().upper()
    if len(comando.split()) > 1:
        comando, valor = comando.split()
    else:
        valor = False
    cpu.executa(comando, int(valor))