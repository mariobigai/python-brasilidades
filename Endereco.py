import re, requests
from warnings import warn

class Endereco:
    def __init__(self, cep):
        self._cep = self._valida_cep(cep)

    def __str__(self):
        if self._extrai_dados() is None:
            return '{} CEP não cadastrado'.format(self._formata_cep())
        else:
            cidade, estado, bairro, ddd, logradouro = self._extrai_dados()
            return 'CEP: {} ; Localidade: {}-{} ; DDD: {}, Logradouro: {}'.format(self._formata_cep(), cidade, estado, ddd, logradouro)

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

    def _acessa_API_viaCEP(self):
        r = requests.get('http://viacep.com.br/ws/{}/json/'.format(self._cep))
        if r.status_code == requests.codes.ok:
            return r
        else:
            warn('API indisponível')

    def _verifica_dados(self, dados):
        return dados.get('erro', False) #Verifica dict de retorno self._acessa_API_viaCEP().json(): 'erro' TRUE - CEP não cadastrado


    def _extrai_dados(self):
        dados = self._acessa_API_viaCEP().json()
        if not self._verifica_dados(dados):
            cidade = dados['localidade']
            estado = dados['uf']
            bairro = dados['bairro']
            ddd = dados['ddd']
            logradouro = dados['logradouro']
            return cidade, estado, bairro, ddd, logradouro
        else:
            return None

