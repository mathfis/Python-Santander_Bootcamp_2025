#importando datetime, criando um objeto date
import datetime
d1 = datetime.date(1986,4,15)
print(d1)

#importando date, criando um objeto date
from datetime import date
d2 = date(2014,4,22)
print(d2)

# importando datetime e time de datetime para produtizr um objetos
from datetime import datetime,time
#horário completo
data_hora = datetime(year=2025,month=8,day=5,
                    hour=12,minute=28,second=59,
                    microsecond=500000) #classe datetime
print(data_hora)
#hoje
hoje = datetime.today() #método today da classe datetime
print(hoje)
#hora qualquer
hora = time(12,31,0) #classe time
print(hora)


"""
Mais informações em https://docs.python.org/pt-br/3/library/datetime.html#module-datetime
"""