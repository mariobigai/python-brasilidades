import re

class Endereco:
    def __init__(self, cep):
        self._cep = self._valida_cep(cep)

    def __str__(self):
        return '{}-{}'.format(self._cep[:5], self._cep[5:])

    def _valida_cep(self, cep):
        cep = str(cep)
        padrao = re.compile('([0-9]{5})(-)?([0-9]{3})')
        combina = padrao.search(cep)
        if len(cep) == 8 and combina != None:
            return combina.group(1) + combina.group(3)
        else:
            raise ValueError("CEP inválido")

