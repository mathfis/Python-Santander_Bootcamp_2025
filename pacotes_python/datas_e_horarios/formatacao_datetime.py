# Formatação usando strftime e strptime

from datetime import datetime # importando a classe datetime do módulo datetime

# imprimindo string com data no formato desejado
d = datetime.now() #utilizando o método now() da classe datetime
d_formatada = d.strftime("%d/%m/%Y %H:%M") #colocando a string no formato desejado
print(d_formatada)

#recebendo uma string formatada e transformando em tipo datetime
d_formatada = "06/08/2025 10:03"
d = datetime.strptime(d_formatada,"%d/%m/%Y %H:%M")
print(d)

# retirando apenas a data do objeto e apresentando em formato brasileiro
d_brasa = d.strftime("%d/%m/%Y")
print(d_brasa)


# formato brasileiro com dia da semana em inglês usando %a
d_brasa = d.strftime("%a, %d/%m/%Y")
print(d_brasa)

#dia da semana em português brasileiro
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
d_brasa = d.strftime("%a, %d/%m/%Y")
print(d_brasa)
 
"""
Mais informações em https://docs.python.org/pt-br/3/library/datetime.html#module-datetime
"""