class Timer:
  def __init__(self):
    self.__contador = 0
    self.__lista_interrupcoes = []

  def incrementa(self):
    self.__contador += 1

  def getTempoAtual(self):
    return self.__contador

  def cheackInterrupcaoPendente(self):
    if len(self.__lista_interrupcoes) > 0:
      if self.__contador == self.__lista_interrupcoes[0]['TEMPO']:
        if self.__lista_interrupcoes[0]['TIPO'] == 'periodica':
          self.__lista_interrupcoes[0]['TEMPO'] = self.__lista_interrupcoes[0]['TEMPO'] + self.__lista_interrupcoes[0]['PERIODO']
          self.__lista_interrupcoes = sorted(self.__lista_interrupcoes, key= lambda x : x['TEMPO'])
          return self.__lista_interrupcoes[0]['CODIGO']
        else:
          interrupcao = self.__lista_interrupcoes[0]
          print(f'LISTA INTERRUP : {self.__lista_interrupcoes}')
          self.__lista_interrupcoes = self.__lista_interrupcoes[1:]
          print(f'removido interrupcao {interrupcao}')
          return interrupcao['CODIGO']
      else:
        return -1
    else:
      return -1

  def criaInterrupcao(self, tipo, periodo, tempo, codigo):
    interrupcao = {'CODIGO': codigo,
                    "TIPO" : tipo,
                    "TEMPO": tempo + self.__contador,
                    "PERIODO": periodo #intervalo
                  }

    self.__lista_interrupcoes.append(interrupcao)
    self.__lista_interrupcoes = sorted(self.__lista_interrupcoes, key= lambda x : x['TEMPO'])
    

