# Trabalhando com time zone usando pytz
from datetime import datetime, timedelta,timezone

print(2*"\t","São Paulo", 3*"\t", "Oslo")

# Sem pytz
fusos = [-3, 2]
d_sp, d_oslo = [datetime.now(timezone(timedelta(hours=h))) for h in fusos]
print("normal\t",d_sp, d_oslo)

# pip install pytz
import pytz 

timezones = ["America/Sao_Paulo","Europe/Oslo"]
d_sp, d_oslo = [datetime.now( pytz.timezone(tz) ) for tz in timezones]
print("pytz\t",d_sp,d_oslo)

"""
Mais informações em https://docs.python.org/pt-br/3/library/datetime.html#module-datetime
"""