class Timer:
  def __init__(self):
    self._contador = 0
    self._lista_interrupcoes = []

  def incrementa(self):
    self._contador += 1

  def tempo_atual(self):
    return self._contador

  def pendencia(self):
    if len(self._lista_interrupcoes) > 0:
      if self._contador == self._lista_interrupcoes[0]['TEMPO']:
        if self._lista_interrupcoes[0]['TIPO'] == 'periodica':
          self._lista_interrupcoes[0]['TEMPO'] = self._lista_interrupcoes[0]['TEMPO'] + self._lista_interrupcoes[0]['PERIODO']
          self._lista_interrupcoes = sorted(self._lista_interrupcoes, key= lambda x : x['TEMPO'])
          return self._lista_interrupcoes[0]['CODIGO']
        else:
          interrupcao = self._lista_interrupcoes[0]
          self._lista_interrupcoes = self._lista_interrupcoes[1:]
          print(f'removido interrupcao {interrupcao}')
          return interrupcao['CODIGO']
      else:
        return False
    else:
      return False

  def interrupcao(self, tipo, periodo, tempo, codigo):
    interrupcao = {'CODIGO': codigo,
                    "TIPO" : tipo,
                    "TEMPO": tempo + self._contador,
                    "PERIODO": periodo #intervalo
                  }

    self._lista_interrupcoes.append(interrupcao)
    self._lista_interrupcoes = sorted(self._lista_interrupcoes, key= lambda x : x['TEMPO'])
    