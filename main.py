import re
from TelefonesBR import TelefonesBR

texto = "meu numero e (17)98105-4166"
telefone = TelefonesBR(texto)
print(telefone._telefone)