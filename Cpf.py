from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.formata_cpf()

    def valida_cpf(self, documento):
        if len(documento) == 11:
            validador = CPF(documento)
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)