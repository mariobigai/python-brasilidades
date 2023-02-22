import re

class TelefonesBR:
    def __init__(self, telefone):
        self._telefone = self._valida(telefone)

    def _valida(self, telefone):
        padrao = re.compile("(\()?[0-9]{2}(\))?[0-9]{4,5}-?[0-9]{4}")
        combina = padrao.search(telefone)

        if not combina:
            raise ValueError("Telefone inválido")
        return combina.group()

