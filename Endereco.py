import re, requests, warnings

class Endereco:
    def __init__(self, cep):
        self._cep = self._valida_cep(cep)

    def __str__(self):
        return self._formata_cep()

    def _valida_cep(self, cep):
        cep = str(cep)
        padrao = re.compile('([0-9]{5})(-)?([0-9]{3})')
        combina = padrao.search(cep)
        if (len(cep) == 8 or len(cep) == 9) and combina != None: #testa se cep tem 8 ou 9 caracteres e se o padrão foi encontrado
            return combina.group(1) + combina.group(3)
        else:
            raise ValueError("CEP inválido")

    def _formata_cep(self):
        return '{}-{}'.format(self._cep[:5], self._cep[5:])

    def acessa_via_cep(self):
        r = requests.get('http://viacep.com.br/ws/{}/json/'.format(self._cep))
        if r.status_code == requests.codes.ok:
            return r
        else:
            warn('API indisponível')


