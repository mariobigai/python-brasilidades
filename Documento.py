from validate_docbr import CPF,CNPJ

class Documento:
    @staticmethod
    def cria_novo(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

class DocCPF:
    def __init__(self, documento):
        if self._valida(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self._formata()

    def _valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def _formata(self):
        mascara = CPF()
        return mascara.mask(self._cpf)


class DocCNPJ:
    def __init__(self, documento):
        if self._valida(documento):
            self._cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def __str__(self):
        return self._formata()

    def _valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def _formata(self):
        mascara = CPF()
        return mascara.mask(self._cnpj)