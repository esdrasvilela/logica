import datetime
import calendar
from babel.dates import format_date

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
               "sexta-feira", "sábado", "domingo"]
# 21/12/2024
data = datetime.date(2024, 12, 21)
print(data)

hoje = datetime.date.today()

hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month]} de {hoje.year}")



print(f"2028 é Bissexto: {calendar.isleap(2028)}")
print(f"O ultimo dia do mês é dia: {calendar.monthrange(2026, 10)[1]}")