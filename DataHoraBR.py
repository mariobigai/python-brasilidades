import datetime

class DataHoraBR:
    def __init__(self):
        self._data_hora = datetime.datetime.today()

    def __str__(self):
        return self._formata()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self._data_hora.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda-feira", "terça-feira",
            "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado", "domingo"
        ]

        dia_semana = self._data_hora.weekday()
        return dia_semana_lista[dia_semana]

    def _formata(self):
        return self.dia_semana() + " - " + self._data_hora.strftime("%d/%m/%Y - %H:%M:%S")
