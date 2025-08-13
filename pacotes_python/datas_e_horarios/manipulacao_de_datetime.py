#importando datetime, obtendo a data de agora através do método today()

from datetime import datetime
agora = datetime.today()
print(f"\nAgore é: {agora}")

#para usar timedelta
from datetime import timedelta

#60 horas
daqui_60_horas = agora + timedelta(hours=60)
print(f"daqui 60 horas : {daqui_60_horas}")

# Obtendo a data da semana que vem
semana_que_vem = agora + timedelta(weeks=1)
print(f"semana que vem : {semana_que_vem.date()}\n")


"""
Mais informações em https://docs.python.org/pt-br/3/library/datetime.html#module-datetime
"""