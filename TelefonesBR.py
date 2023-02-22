import re

class TelefonesBR:
    def __init__(self, telefone):
        self._telefone = self._formata(telefone)

    def __str__(self):
        return self._telefone

    def _valida(self, telefone):
        padrao = re.compile("(\+)?([0-9]{2,3})?(\()?([0-9]{2})(\))?([0-9]{4,5})(-)?([0-9]{4})")
        combina = padrao.search(telefone)

        if not combina:
            raise ValueError("Telefone inválido")
        return combina

    def _formata(self, telefone):
        numero_entrada = self._valida(telefone)

        numero_formatado = "+{}({}){}-{}".format(
            numero_entrada.group(2),
            numero_entrada.group(4),
            numero_entrada.group(6),
            numero_entrada.group(8)
        )

        if numero_entrada.group(2) == None:
            numero_formatado = numero_formatado.replace('None', '55')

        return numero_formatado